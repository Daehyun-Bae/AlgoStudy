#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
//int *arr, *sub, SIZE_sub;
vector<int> raw;
vector<vector<int>> tree;

vector<int> merge(vector<int> a, vector<int> b) {
	if (a.empty()) return b; if (b.empty()) return a;

	vector<int> tmp; 
	int a_id = 0, b_id = 0;

	while (a_id < a.size() && b_id < b.size()) {
		if (a[a_id] < b[b_id]) tmp.push_back(a[a_id++]);
		else tmp.push_back(b[b_id++]);
	}
	while (a_id < a.size()) { tmp.push_back(a[a_id++]); }
	while (b_id < b.size()) { tmp.push_back(b[b_id++]); }
	return tmp;
}

vector<int> init(int start, int end, int index) {
	if (start == end) {
		vector<int> tmp; tmp.push_back(raw[start]);
		return tree[index] = tmp;
	}
	return tree[index] = merge(init(start, (start + end) / 2, index * 2), init((start + end) / 2 + 1, end, index * 2 + 1));
}

void split(int left, int right, int start, int end, int index, vector<int> & a) {
	if (start < left || right < end) {
		return;
	}
	else if (left <= start && end <= right) {
		a.push_back(index);
		return;
	}
	split(left, right, start, (start + end) / 2, index * 2, a);
	split(left, right, (start + end) / 2 + 1, end, index * 2 + 1, a);
}

pair<int, int> count(vector<int> & a, int k, int index) {
	int low = 0, high = 0;
	for (auto i : a) {
		low += (int)(lower_bound(tree[i].begin(), tree[i].end(), index) - tree[i].begin());
		high += (int)(upper_bound(tree[i].begin(), tree[i].end(), index) - tree[i].begin());
	}
	return{ low, high };
}

int main() {
	int T, Size, i, j, k;
	cin >> Size >> T;
	raw.resize(Size + 10);
	tree.resize(Size * 4 + 10);

	for (int i = 1; i <= Size; i++) {
		cin >> raw[i];
	}
	
	init(1,Size, 1);
	while (T--) {
		vector<int> tmp;
		cin >> i >> j >> k;
		split(i, j, 1, Size, 1, tmp);
		
		int left = tree[1].front() - 1, right = tree[1].back() + 1, mid;

		while (left <= right) {
			if ((left + right) >= 0) mid = (left + right) / 2;
			else mid = (left + right - 1) / 2;
			
			auto cnt = count(tmp, k, mid);
			cout << "left: " << left << "right: " << right << "mid: " << mid <<"first: "<< cnt.first<<"second: "<< cnt.second<< endl;
			if (cnt.first <= k - 1 && cnt.second >= k) break;
			else if (cnt.first <= k - 1) left = mid + 1;
			else right = mid;
		}
		cout << mid << endl;
	}


	/*
	arr = new int[Size + 1];
	for (int i = 1; i <= Size; i++) {
		cin >> tmp;
		arr[i] = tmp;
	}
	while (T--) {
		cin >> i >> j >> k;
		Q(i, j, k);
	}*/
}

/*********************************

// using for debuging
void print_arr(int *arr) {
for (int i = 0; i < SIZE_sub; i++) cout << arr[i] << " ";
cout << endl;
}

void sort(int *arr) {
int i, j;
for (i = 0; i < SIZE_sub; i++) {
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
*********************/
