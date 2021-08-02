#include <stdio.h>
#include <queue>
using namespace std;

int chess[55][55];
int make[55][55];
int ans[55][55];
int w, h;

int dx[4] = { 1,-1,0,0 };
int dy[4] = { 0,0,-1,1 };

void init();

int find(int x, int y);


int main() {



	char color[100];
	int i, j,k;
	int min = 100;
	int cnt = 0;
	scanf("%d", &h);
	scanf("%d", &w);

	for (i = 1; i <= h; i++) {
		scanf("%s", color);
		for (k = 0; k < w; k++) {
			if (color[k] == 'B')
				make[i][k + 1] = 1;
		}
	}

	init();
	for (i = 1; i <= h - 7; i++) {
		for (j = 1; j <= w - 7; j++) {
			cnt = find(i, j);
			if (min > cnt)
				min = cnt;

		}
	}
	printf("%d", min);


}

void init() {
	int i, j;
	int cnt = 0;
	for (i = 1; i < 55; i++) {
		for (j = 1; j < 55; j++) {
			if (cnt % 2==0)
				chess[i][j] = 1;
			else
				chess[i][j] = 0;
			cnt++;
		}
		cnt++;
	}
}

int find(int x,int y) {
	int i, j;
	int cnt = 0;
	for (i = 0; i < 8; i++) {
		for (j = 0; j < 8; j++) {
			if (make[i + x][j + y] == chess[i + 1][j + 1])
				cnt++;
		}
	}
	if (cnt > 32)
		return 64 - cnt;
	else
		return cnt;
}

