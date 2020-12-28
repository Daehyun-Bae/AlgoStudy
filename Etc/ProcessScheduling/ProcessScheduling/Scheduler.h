#define MAX 100


struct Process {
	int PID, AT, Cycle, CPU_burst, IO_burst;
};

struct queue {
	Process ready[MAX];
	int TQ;
	int top;
};

void enQ(queue *q, Process p) {
	q->ready[q->top++] = p;
}

Process deQ(queue *q) {
	int i;
	Process tmp;
	if (isEmpty(q)) return;
	tmp = q->ready[0];
	for (i = 0; i < q->top - 1; i++) q->ready[i] = q->ready[i + 1];
	return tmp;
}

bool isEmpty(queue *q) {
	return q->top == 0;
}