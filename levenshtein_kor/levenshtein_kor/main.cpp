#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <locale>
#include <algorithm>
#define Max_SIZE 100
#define first 0xAC00	// first Korean code val
#define last 0xD7AF		// last Korean code val
using namespace std;


wstring str1, str2;
vector <wchar_t> v1, v2;
wchar_t buf_I, buf_M, buf_F;
int dist[Max_SIZE][Max_SIZE];

const wchar_t init[] = {
	L'ぁ', L'あ', L'い', L'ぇ',
	L'え', L'ぉ', L'け', L'げ',
	L'こ', L'さ', L'ざ', L'し',
	L'じ', L'す', L'ず', L'せ',
	L'ぜ', L'そ', L'ぞ' };
const wchar_t med[] = {
	L'た', L'だ', L'ち', L'ぢ',
	L'っ', L'つ', L'づ', L'て',
	L'で', L'と', L'ど', L'な',
	L'に', L'ぬ', L'ね', L'の',
	L'は', L'ば', L'ぱ', L'ひ', L'び' };
const wchar_t fin[] = {
	L' ', L'ぁ', L'あ', L'ぃ',
	L'い', L'ぅ', L'う', L'ぇ',
	L'ぉ', L'お', L'か', L'が',
	L'き', L'ぎ', L'く', L'ぐ',
	L'け', L'げ', L'ご', L'さ',
	L'ざ', L'し', L'じ', L'ず',
	L'せ', L'ぜ', L'そ', L'ぞ' };

int levenshtein(vector <wchar_t> str1, vector <wchar_t> str2);
void kor_Decomp(wchar_t w) {
	if (w >= first && w <= last) {
		int i, m, f;
		int tmp = (int)w - first;
		f = tmp % 28;
		m = ((tmp - f) / 28) % 21;
		i = (((tmp - f) / 28) - m) / 21;
		buf_I = init[i];
		buf_M = med[m];
		buf_F = fin[f];				// set each element to buffer
		return;
	}
	return;
}
int main() {
	wcin.imbue(locale("korean"));
	wcout.imbue(locale("korean"));
	int n=1;
	while (n == 1) {
		cout << "type two words..." << endl;	// input 2 words
		wcin >> str1 >> str2;
		for (int i = 0; i < str1.length(); i++) {
			kor_Decomp(str1[i]);
			v1.push_back(buf_I);
			v1.push_back(buf_M);
			v1.push_back(buf_F);			// decompose first word and save in vector1
		}
		for (int i = 0; i < str2.length(); i++) {
			kor_Decomp(str2[i]);
			v2.push_back(buf_I);
			v2.push_back(buf_M);
			v2.push_back(buf_F);			// decompose second word and save in vector2
		}
		
		cout << "\nresult: " << levenshtein(v1, v2) << endl;
		v1.clear(); v2.clear();
		cout << "continue? yes=1" << endl;
		cin >> n;
	}
}

int levenshtein(vector <wchar_t> str1, vector <wchar_t> str2) {
	int w;
	for (int i = 1; i <= str1.size(); i++) dist[i][0] = ((str1.size() - i) + str2.size()) + 1;
	for (int i = 1; i <= str2.size(); i++) dist[0][i] = ((str2.size() - i) + str1.size()) + 1;	// initialize first column and row

	for (int i = 1; i <= str1.size(); i++) {
		for (int j = 1; j <= str2.size(); j++) {
			w = ((str1.size() - i) + (str2.size() - j)) + 1;
			if (str1[i - 1] == str2[j - 1]) dist[i][j] = dist[i - 1][j - 1];
			else dist[i][j] = min(dist[i - 1][j - 1] + w, min(dist[i][j - 1] + w, dist[i - 1][j] + w));
		}
	}		
	printf("\n\t\t");
	for (int i = 0; i < v2.size(); i++) {
		wcout << v2[i] << "\t";
	}
	printf("\n");
	for (int i = 0; i <= str1.size(); i++) {
		if (i != 0)wcout << v1[i - 1] << "\t";
		else printf("\t");
		for (int j = 0; j <= str2.size(); j++) {
			printf("%d\t", dist[i][j]);
		}
		printf("\n");
	}
	return dist[str1.size()][str2.size()];
}
