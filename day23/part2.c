#include <assert.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define LEN(x) (sizeof(x) / sizeof((x)[0]))
#define DIFF ((int[4]){cols, -cols, 1, -1})

char grid[65536];
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

struct distmap_node {
	struct distmap_node *next;
	int p, q;
	int dist;
};

struct distmap_node *distmap[1009] = {0};

int
distance(int p, int q)
{
	int hash = (p + q * 3) % LEN(distmap);
	struct distmap_node *dmn;
	for (dmn = distmap[hash]; dmn != NULL; dmn = dmn->next)
		if (dmn->p == p && dmn->q == q)
			return dmn->dist;

	struct state {
		int pos;
		int dist;
	} stack[1024] = {{p, 0}};

	bool seen[LEN(grid)] = {0};
	int maxdist = 0;
	int k = 1;
	while (k > 0) {
		assert(k < LEN(stack));

		k--;
		int r = stack[k].pos;
		int dist = stack[k].dist;

		if (r == q) {
			if (dist > maxdist)
				maxdist = dist;
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
				stack[k].dist = dist + 1;
				k++;
			}
		}
	}

	dmn = malloc(sizeof(*dmn));
	dmn->p = p;
	dmn->q = q;
	dmn->dist = maxdist;
	dmn->next = distmap[hash];
	distmap[hash] = dmn;
	return maxdist;
}

int
neighbors(int p, int **res)
{
	static int cache[LEN(grid)][5];

	if (*cache[p])
		goto ret;

	bool seen[LEN(grid)] = {0};
	int stack[1024] = {p};
	int k = 1;
	int n = 0;
	while (k > 0) {
		assert(k < LEN(stack));

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
	static bool seen[LEN(grid)];

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
