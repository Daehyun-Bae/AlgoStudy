/*#include <GL/glut.h> 
#include <GL/glu.h>

float r, g, b;

void display() {
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);		// clear GL buffers
	glLoadIdentity();									// Reset our view
	glBegin(GL_QUADS); // Draw a rectangle
	glColor3f(r, g, b); 
	glVertex3f(-0.5f, -0.5f, 0.0f); 
	glVertex3f(-0.5f, 0.5f, 0.0f); 
	glVertex3f(0.5f, 0.5f, 0.0f); 
	glVertex3f(0.5f, -0.5f, 0.0f);
	glEnd(); 
	glFlush();		// force to execute all pending commands
}
void keyboardInput(unsigned char key, int x, int y) {
	if (key == 'r') {
		r = 1.0, g = 0.0, b = 0.0;
	}
	else if (key == 'g') {
		r = 0.0, g = 1.0, b = 0.0;
	}
	else if (key == 'b') {
		r = 0.0, g = 0.0, b = 1.0;
	}
	else {
		r = 1.0, g = 1.0, b = 1.0;
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
int main(int argc, char** argv) {
	glutInit(&argc, argv); 
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA | GLUT_DEPTH); 
	glutInitWindowSize(512, 512); 
	glutCreateWindow("CG Lab 1"); 
	glutDisplayFunc(display);
	glutKeyboardFunc(keyboardInput);
	glutMouseFunc(mouse);
	glutMainLoop(); 
	return 0;
}*/