#include <stdio.h>
#include <stdlib.h>


int CNT_0;
int CNT_1;

int ary_1[100];
int ary_0[100];

int main() {
	int tries;
	int i, j;
	int num;
	int *ans_idx;
	scanf("%d", &tries);

	ary_0[0] = 1;
	ary_1[1] = 1;

	for (i = 2; i <= 41; i++) {

		ary_1[i] = ary_1[i - 1] + ary_1[i - 2];
		ary_0[i] = ary_0[i - 1] + ary_0[i - 2];
	}

	ans_idx = (int*)malloc(sizeof(int)*tries);






	for (i = 0; i < tries; i++) {
		scanf("%d", &ans_idx[i]);
	}

	for (i = 0; i < tries; i++) {
		printf("%d %d\n", ary_0[ans_idx[i]], ary_1[ans_idx[i]]);
	}

	
}
