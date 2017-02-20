#include <iostream>
#include <algorithm>
#include <string.h>
#define MAX_LIST 20
#define TABLE_SIZE 201

using namespace std;

int main() {
	int Case;
	unsigned int knap[TABLE_SIZE];
	// input Num.Test Case
	cin >> Case;
	while (Case--) {
		memset(knap, 0, sizeof(knap));
		int N;
		long long B;
		long long price[MAX_LIST];
		unsigned int pref[MAX_LIST];
		// input Num.menu types, Budget
		cin >> N >> B;
		B /= 100;
		// input Data
		for (int i = 0; i < N; i++) {
			cin >> price[i] >> pref[i];
			price[i] /= 100;
		}
		
		for (int p = 1; p <= B; p++) {
			unsigned int& x = knap[p % TABLE_SIZE];
			x = 0;
			for (int i = 0; i < N; i++) {
				if (p >= price[i])
					x = max<unsigned int>(x, knap[(p - price[i]) % TABLE_SIZE] + pref[i]);
			}
		}
		
		cout << knap[B % TABLE_SIZE] << endl;
	}
	return 0;
}