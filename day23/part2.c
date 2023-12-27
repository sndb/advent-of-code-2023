#include <assert.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

#define N 20000
#define DIFF ((int[4]){cols, -cols, 1, -1})

char grid[N];
int rows, cols, goal;

bool
valid(int p)
{
	return p >= 0 && p < rows * cols && grid[p] != '#';
}

bool
passage(int p)
{
	if (p == goal)
		return true;

	int a = 0;
	for (int i = 0; i < 4; i++) {
		int q = p + DIFF[i];
		a += valid(q);
	}
	return a > 2;
}

int
distance(int p, int q)
{
	static int cache[N][N];

	int res = cache[p][q];
	if (res)
		return res;

	struct state {
		int pos;
		int dist;
	} stack[1024] = {{p, 0}};

	bool seen[N] = {false};
	int k = 1;
	while (k > 0) {
		assert(k < sizeof(stack) / sizeof(*stack));

		k--;
		int r = stack[k].pos;
		int d = stack[k].dist;

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
				stack[k].pos = s;
				stack[k].dist = d + 1;
				k++;
			}
		}
	}
	cache[p][q] = res;
	return res;
}

int
neighbors(int p, int **res)
{
	static int cache[N][5];

	if (*cache[p])
		goto ret;

	bool seen[N] = {false};
	int stack[1024] = {p};
	int k = 1;
	int n = 0;
	while (k > 0) {
		assert(k < sizeof(stack) / sizeof(*stack));

		k--;
		int q = stack[k];

		if (seen[q])
			continue;
		seen[q] = true;

		if (q != p && passage(q)) {
			cache[p][++n] = q;
			continue;
		}

		for (int i = 0; i < 4; i++) {
			int r = q + DIFF[i];
			if (valid(r))
				stack[k++] = r;
		}
	}
	*cache[p] = n;
ret:
	*res = cache[p] + 1;
	return *cache[p];
}

int answer = 0;

void
search(int p, int d)
{
	static bool seen[N];

	if (p == goal) {
		if (d > answer)
			answer = d;
		return;
	}

	if (seen[p])
		return;
	seen[p] = true;

	int *adj;
	int n = neighbors(p, &adj);
	for (int i = 0; i < n; i++) {
		int q = adj[i];
		search(q, d + distance(p, q));
	}
	seen[p] = false;
}

void
init(void)
{
	int i = 0, r = 0, c;
	while ((c = getchar()) != EOF)
		if (c == '\n')
			r++;
		else
			grid[i++] = c;
	rows = r;
	cols = i / r;
	goal = rows * cols - 2;
}

int
main(void)
{
	init();
	search(1, 0);
	printf("%d\n", answer);
	return 0;
}
