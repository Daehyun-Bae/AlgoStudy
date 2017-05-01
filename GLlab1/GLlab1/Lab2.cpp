#include <GL/glut.h> 
#include <GL/glu.h>

float pos_x = 0.0f, pos_y = 0.0f, pos_z = -4.0f;

void display() { 
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glMatrixMode(GL_MODELVIEW); 
	glLoadIdentity();
	glRotatef(60, 1, 0, 0);
	glTranslatef(pos_x, pos_y, pos_z);
	glColor3f(1.0f, 1.0f, 0.0f); 
	glutWireTeapot(0.5);	// Teapot Model
	glFlush(); 
}
void reshape(int width, int height) {
	glViewport(0, 0, width, height); 
	glMatrixMode(GL_PROJECTION); 
	glLoadIdentity(); 
	double aspect = width / double(height); 
	gluPerspective(45, aspect, 1, 1024);
}
void keyboardInput(unsigned char key, int x, int y) {
	if (key == 'd') {
		pos_x += 0.05f;
	}
	else if (key == 'a') {
		pos_x -= 0.05f;
	}
	else if (key == 'w') {
		pos_y += 0.05f;
	}
	else if (key == 's') {
		pos_y -= 0.05f;
	}
	else if (key == 'm') {
		pos_z += 0.1f;
	}
	else if (key == 'n') {
		pos_z -= 0.1f;
	}
	glutPostRedisplay();
}
int main(int argc, char** argv) {
	glutInit(&argc, argv); 
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA | GLUT_DEPTH); 
	glutInitWindowSize(900, 900); 
	glutCreateWindow("CG Lab 2"); 
	glutReshapeFunc(reshape);
	glutDisplayFunc(display);
	glutKeyboardFunc(keyboardInput);
	glutMainLoop(); 
	return 0;
}