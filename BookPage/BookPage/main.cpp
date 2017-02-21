/* No.1019 in BAEKJOON ONLINE JUDGE
	Coding By DH Bae */
#include <iostream>
#include <string.h>
#include <math.h>
using namespace std;
int cache[10];
int result[10];
int lastDigit(int n) {
	return n % 10;
}
void getResult(int n, int k) {
	int M = 0;
	M = n / 10;
	for (int i = 1; i <= lastDigit(n); i++) cache[i]++;
	for (int i = 0; i < 10; i++) cache[i] += M;
	while (M != 0) {
		cache[lastDigit(M)] += lastDigit(n) + 1;
		M /= 10;
	}
	for (int i = 0; i < 10; i++) result[i] += cache[i] * pow(10, k);
	memset(cache, 0, sizeof(cache));
}
int main() {
	int N, M, tmp;
	cin >> N;
	M = 0;
	tmp = N;
	while (tmp > 0) {
		M++;
		tmp /= 10;
	}
	memset(result, 0, sizeof(result));
	for (int k = 0; k < M; k++) {
		if (N > 0) {
			getResult(N, k);
			N = (N / 10) - 1;
		}
		else break;
	}
	for (int i = 0; i < 9; i++) cout << result[i] << " ";
	cout << result[9];
	return 0;
}