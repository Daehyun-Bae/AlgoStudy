#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>

double size_tri(int a, int b, int c);
double size_ho(int a, double arc);
int main()
{
	int Case, a, b, c;
	double theta1, theta2, pi;
	pi = acos(-1.0);
	scanf("%d", &Case);
	while (Case--) {
		scanf("%d", &a);
		scanf("%d", &b);
		scanf("%d", &c);
		theta1 = asin(2 * size_tri(a, b, c) / (a*c));
		theta2 = asin(2 * size_tri(a, b, c) / (b*c));
		printf("%.3f\n", pow(a, 2)*pi - (size_ho(a, theta1) + size_ho(b, theta2)));
	}
	return 0;
}
double size_tri(int a, int b, int c) {
	double s = (double)(a + b + c) / 2;
	return sqrt(s*(s - a)*(s - b)*(s - c));
}
double size_ho(int a, double arc) {
	return pow(a, 2)*(arc - sin(arc)*cos(arc));
}