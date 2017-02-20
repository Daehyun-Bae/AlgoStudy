#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
#define MAX_LIST 20

using namespace std;

class Dish {
public:
		int price;
		int pref;
		float avg;
		Dish(int price, int pref) {
			this->price = price;
			this->pref = pref;
			avrage();
		};
		void avrage() {
			avg = (float)price / pref;
		}
		void print() {
			cout << "Price: " << price << "\tPrior: "<< pref << "\tAvg: " << avg <<endl;
		}
};
bool operator < (const Dish &a, const Dish &b) {
	return a.avg < b.avg;
}

int main() {
	int Case, n, m, Price, Pref, min, result = 0, sum=0;
	vector <Dish> list;
	//Dish tmp(0, 0);

	// input Num.Test Case
	cin >> Case;
	// input Num.menu types, Budget
	cin >> n >> m;
	// input Data
	//M_avg = 0;
	for (int i = 0; i < n; i++) {
		cin>> Price >> Pref;
		list.push_back(Dish(Price, Pref));
	}
	sort(list.begin(), list.end());
	min = m;
	for (int i = 0; i < n; i++) {
		if (list[i].price <= min) min = list[i].price;
	}
		
	while (1) {
		for (int i = 0; i < n; i++) {
			if (sum + list[i].price < m) {
				sum += list[i].price;
				result += list[i].pref;
				cout << result << endl;
				break;
			}
		}
		if (sum + min > m) break;
	};
	cout << result << endl;
	scanf("%d", &Case);
}