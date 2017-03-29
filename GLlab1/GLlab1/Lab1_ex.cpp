/*#include <iostream>
#include <GL/glut.h> 
#include <GL/glu.h>

using namespace std;

int N;
int **map;
int StartPt_X, StartPt_Y;
float L;

void display() {
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);		// clear GL buffers
	glLoadIdentity();									// Reset our view
	glBegin(GL_QUADS); // Draw a rectangle
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (map[i][j] == 1) {
				glColor3f(0.0, 0.0, 1.0);
			}
			else if (map[i][j] == 2) {
				glColor3f(1.0, 0.0, 0.0);
			}
			else if (map[i][j] == 3) {
				glColor3f(0.0, 1.0, 0.0);
			}
			else if (map[i][j] == 0) {
				glColor3f(0.0, 0.0, 0.0);
			}
		}
	}
	glVertex3f(-1.0f, -0.1f, 0.0f);
	glVertex3f(-0.1f, 0.1f, 0.0f);
	glVertex3f(0.1f, 0.1f, 0.0f);
	glVertex3f(0.1f, -0.1f, 0.0f);
	glEnd();
	glFlush();		// force to execute all pending commands
}
void keyboardInput(unsigned char key, int x, int y) {
	if (key == 'a') {
		StartPt_X--;
	}
	else if (key == 'w') {
		
	}
	else if (key == 's') {
		
	}
	else if (key == 'd') {
		
	}
	glutPostRedisplay();
}
void mouse(int button, int state, int x, int y) {
	if ((button == GLUT_LEFT_BUTTON) && (state == GLUT_DOWN)) {
		r = 1.0, g = 1.0, b = 0.0;
		display();
	} if ((button == GLUT_RIGHT_BUTTON) && (state == GLUT_DOWN)) {
		r = 1.0, g = 0.0, b = 1.0; display();
	}
}
void read_map(const char *filename) {
	FILE *input = fopen(filename, "r");
	fscanf(input, "%d", &N);
	map = new int*[N];
	for (int i = 0; i < N; i++) {
		map[i] = new int[N];
		for (int j = 0; j < N; j++) {
			for (int k = 0; k < N; k++) {
				fscanf(input, "%d", &map[j][k]);
				if (map[j][k] = 2) {
					StartPt_X = k, StartPt_Y = j;
				}
			}
		}
	}
	fclose(input);
}
int main(int argc, char** argv) {
	//read_map("map.txt");

	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA | GLUT_DEPTH);
	glutInitWindowSize(512, 512);
	glutCreateWindow("CG Lab 1 - Excercise");
	glutDisplayFunc(display);
	glutKeyboardFunc(keyboardInput);
	glutMouseFunc(mouse);
	glutMainLoop();
	return 0;
}*/