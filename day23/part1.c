#include <stdbool.h>
#include <stdio.h>

#define N 20000

char grid[N];
int rows, cols, goal;
int answer = 0;

void
search(int p, int dist)
{
	static bool seen[N];

	if (p == goal) {
		if (dist > answer)
			answer = dist;
		return;
	}

	if (seen[p])
		return;
	seen[p] = true;

	if (grid[p] == '>') {
		search(p + 1, dist + 1);
	} else if (grid[p] == 'v') {
		search(p + cols, dist + 1);
	} else {
		int diff[4] = {cols, -cols, 1, -1};
		for (int i = 0; i < 4; i++) {
			int np = p + diff[i];
			if (np >= 0 && np < rows * cols && grid[np] != '#')
				search(np, dist + 1);
		}
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
