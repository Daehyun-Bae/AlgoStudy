#include <iostream>
using namespace std;
class Point {
public:
	int x;
	int y;
public : 
	Point() {
	}
	void input(int x, int y){
		this->x = x;
		this->y = y;
	}
};
int main() {
	int T, x, y;
	Point p[4];
	cin >> T;
	while(T--){
		for (int i = 0; i < 3; i++) {
			cin >> x >> y;
			p[i].input(x, y);
		}
		if (p[0].x == p[1].x) {
			x = p[2].x;
		}
		else if (p[1].x == p[2].x) {
			x = p[0].x;
		}
		else {
			x = p[1].x;
		}

		if (p[0].y == p[1].y) {
			y = p[2].y;
		}
		else if (p[1].y == p[2].y) {
			y = p[0].y;
		}
		else {
			y = p[1].y;
		}
		p[3].input(x, y);
		cout << p[3].x << " " << p[3].y << endl;
	}
}