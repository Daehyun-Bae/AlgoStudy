#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <algorithm>

using namespace std;
struct Digit {
	int num, index;
};
Digit Number[100001];

bool comp(const Digit &a, const Digit &b) {
	return a.num < b.num;
}
int main() {
	int N, T, l, r, k;
	scanf("%d %d", &N, &T);
	for (int i = 1; i <= N; i++) {
		scanf("%d", &Number[i].num);
		Number[i].index = i;
	}
	sort(Number + 1, Number + N + 1, comp);

	while (T--) {
		scanf("%d %d %d", &l, &r, &k);
		int cnt = 0;
		for (int i = 1; i <= N; i++) {
			if (Number[i].index >= l && Number[i].index <= r) cnt++;
			if (cnt == k) {
				printf("%d\n", Number[i].num);
				break;
			}
		}
	}
}