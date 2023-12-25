#include <stdbool.h>
#include <stdio.h>

#define N 20000

char grid[N];
int rows = 0;
int cols = 0;

bool seen[N] = {false};
int answer = 0;

void search(int p, int d)
{
	if (p == rows * cols - 2) {
		if (d > answer)
			answer = d;
		return;
	}

	if (seen[p])
		return;
	seen[p] = true;

	if (grid[p] == '>') {
		search(p + 1, d + 1);
	} else if (grid[p] == 'v') {
		search(p + cols, d + 1);
	} else {
		int diff[4] = {cols, -cols, 1, -1};
		for (int i = 0; i < 4; i++) {
			int np = p + diff[i];
			if (np >= 0 && np < rows * cols && grid[np] != '#')
				search(np, d + 1);
		}
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
