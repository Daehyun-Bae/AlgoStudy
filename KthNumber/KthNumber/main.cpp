#include <iostream>

using namespace std;
int *arr, *sub, SIZE_sub;

// using for debuging
void print_arr(int *arr) {
	for (int i = 0; i < SIZE_sub; i++) cout << arr[i] << " ";
	cout << endl;
}

void sort(int *arr) {
	int i = 0, j;
	for (; i < SIZE_sub; i++) {
		for (j = i; j < SIZE_sub; j++) {
			if (arr[j] <= arr[i]) swap(arr[i], arr[j]);
		}
	}
}

void Q(int i, int j, int k) {
	sub = new int[j - i + 1];
	SIZE_sub = j - i + 1;
	int tmp_i = i, tmp_j = j;
	for (; i <= j; i++) sub[i - tmp_i] = arr[i];
	sort(sub);
	cout << sub[k - 1]<< endl;
	delete sub;
}
int main() {
	int T, Size, tmp, i, j, k;
	cin >> Size >> T;
	arr = new int[Size + 1];
	for (int i = 1; i <= Size; i++) {
		cin >> tmp;
		arr[i] = tmp;
	}
	while (T--) {
		cin >> i >> j >> k;
		Q(i, j, k);
	}
}