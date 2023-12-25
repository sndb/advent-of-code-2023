#include <assert.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

#define N 20000
#define DIFF ((int[4]){cols, -cols, 1, -1})
#define LEN(x) (sizeof(x) / sizeof(*x))

char grid[N];
int rows = 0;
int cols = 0;

bool valid(int p)
{
	return p >= 0 && p < rows * cols && grid[p] != '#';
}

bool goal(int p)
{
	return p == rows * cols - 2;
}

bool passage(int p)
{
	if (goal(p))
		return true;

	int a = 0;
	for (int i = 0; i < 4; i++) {
		int q = p + DIFF[i];
		a += valid(q);
	}
	return a > 2;
}

int distance_cache[N][N] = {0};

int distance(int p, int q)
{
	int c = distance_cache[p][q];
	if (c)
		return c;

	bool seen[N] = {false};
	int pqueue[1024] = {p};
	int dqueue[LEN(pqueue)] = {0};
	int k = 1;
	int res = 0;
	while (k > 0) {
		assert(k < LEN(pqueue));

		k--;
		int r = pqueue[k];
		int d = dqueue[k];

		if (r == q) {
			if (d > res)
				res = d;
			continue;
		}

		if (r != p && passage(r))
			continue;

		if (seen[r])
			continue;
		seen[r] = true;

		for (int i = 0; i < 4; i++) {
			int s = r + DIFF[i];
			if (valid(s)) {
				pqueue[k] = s;
				dqueue[k] = d + 1;
				k++;
			}
		}
	}
	distance_cache[p][q] = res;
	return res;
}

int neighbors_cache[N][4];
int neighbors_cache_len[N] = {0};

int neighbors(int p, int *res)
{
	int cl = neighbors_cache_len[p];
	if (cl) {
		for (int i = 0; i < cl; i++)
			res[i] = neighbors_cache[p][i];
		return cl;
	}

	bool seen[N] = {false};
	int queue[1024] = {p};
	int k = 1;
	int n = 0;
	while (k > 0) {
		assert(k < LEN(queue));

		k--;
		int q = queue[k];

		if (seen[q])
			continue;
		seen[q] = true;

		if (q != p && passage(q)) {
			*res++ = q;
			neighbors_cache[p][n++] = q;
			continue;
		}

		for (int i = 0; i < 4; i++) {
			int r = q + DIFF[i];
			if (valid(r))
				queue[k++] = r;
		}
	}
	neighbors_cache_len[p] = n;
	return n;
}

bool seen[N] = {false};
int answer = 0;

void search(int p, int d)
{
	if (goal(p)) {
		if (d > answer)
			answer = d;
		return;
	}

	if (seen[p])
		return;
	seen[p] = true;

	int adj[4];
	int n = neighbors(p, adj);
	for (int i = 0; i < n; i++) {
		int q = adj[i];
		search(q, d + distance(p, q));
	}
	seen[p] = false;
}

void prepare(void)
{
	int i = 0;
	for (int c; (c = getchar()) != EOF;) {
		grid[i++] = c;
		if (c == '\n') {
			i--;
			rows++;
		}
	}
	cols = i / rows;
}

int main(void)
{
	prepare();
	search(1, 0);
	printf("%d\n", answer);
	return 0;
}
