#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

#define Max_SIZE 100
string str1, str2;
int dist[Max_SIZE][Max_SIZE];

int levenshtein(string& str1, string& str2);

int main() {
	cout << "type two words..." << endl;
	cin >> str1 >> str2;

	cout << "result: " << levenshtein(str1, str2) << endl;
	cin >> str1;
}

int levenshtein(string& str1, string& str2) {
	for (int i = 1; i <= str1.length(); i++) dist[i][0] = i;
	for (int i = 1; i <= str2.length(); i++) dist[0][i] = i;		// initialize first column and row

	for (int i = 1; i <= str1.length(); i++) {
		for (int j = 1; j <= str2.length(); j++) {
			if (str1[i - 1] == str2[j - 1]) dist[i][j] = dist[i - 1][j - 1];
			else dist[i][j] = min(dist[i - 1][j - 1] + 1, min(dist[i][j - 1] + 1, dist[i - 1][j] + 1));
		}
	}
	cout << "\t\t";
	for (int i = 0; i <= str2.length(); i++) printf("%c\t", str2[i]);
	cout << endl;
	for (int i = 0; i <= str1.length(); i++) {
		if (i == 0) printf("\t");
		else printf("%c\t", str1[i-1]);
		for (int j = 0; j <= str2.length(); j++) {
			printf("%d\t", dist[i][j]);
		}
		printf("\n");
	}
	return dist[str1.length()][str2.length()];
}
