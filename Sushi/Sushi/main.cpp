#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#define MAX_LIST 20

struct Dish {
	int price;
	int prior;
	float avg;
	Dish() {
	};
	void avrage() {
		avg = (float)price / prior;
	}
	void print() {
		printf("Price: %d\tPrior: %d\tAvg: %f.2\n", price, prior, avg);
	}
};

int main() {
	int Case, n, m, i, j, sort[MAX_LIST];
	Dish list[MAX_LIST];
	Dish tmp;

	// input Num.Test Case
	scanf("%d", &Case);
	// input Num.people, Budget
	scanf("%d %d", &n, &m);
	// input Data
	i = 0;
	while (n--) {
		scanf("%d %d", &tmp.price, &tmp.prior);
		tmp.avrage();
		list[i] = tmp;
		i++;
	}

	scanf("%d", &Case);
}