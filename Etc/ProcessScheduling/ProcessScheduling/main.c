#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

#define MAX 100
#define CYCLE_SIZE 10


typedef struct{
	int PID, AT, Cycle, cur_cycle, CPU_burst[CYCLE_SIZE], IO_burst[CYCLE_SIZE];
	int home, time_T, total_B;
}Process;

typedef struct{
	Process ready[MAX];
	int TQ;
	int top;
}queue;

Process prcList[MAX];
queue Q0, Q1, Q2, SLEEP;
queue* Qlist[MAX] = { &Q0, &Q1, &Q2 };
int T, time = 0, front = 0;

int isEmpty(queue *q) {
	return q->top == 0;
}

void enQ(queue *q, Process p) {
	q->ready[q->top++] = p;
}

void deQ(queue *q, int base) {
	int i;
	if (isEmpty(q)) return;
	q->top--;
	for (i = base; i < q->top; i++) q->ready[i] = q->ready[i + 1];
}

Process popQ(queue *q, int i) {
	return q->ready[i];
}

void mov_Prc(queue *src, queue *dst, int i) {
	enQ(dst, src->ready[i]);
	deQ(src, i);
}

void show_PrcInfo(Process *p) {
	int i = p->cur_cycle;
	printf("TIME-%d\n\tPID\tAT\tCycle\tCur_cycle\tCPU_burst\tIO_burst\tHOME\n\t%d\t%d\t%d\t%d\t\t%d\t\t%d\t\t%d\n",
		time, p->PID, p->AT, p->Cycle, p->cur_cycle, p->CPU_burst[i], p->IO_burst[i], p->home);
}
void show_SLP_list() {
	printf("\t===SLEEP List===\n");
	int i;
	for (i = 0; i < SLEEP.top; i++) {
		show_PrcInfo(&SLEEP.ready[i]);
	}
	printf("\t=======end======\n");
}
void check_SLP() {
	int i;
	for (i = 0; i < SLEEP.top; i++) {
		if (SLEEP.ready[i].IO_burst[SLEEP.ready[i].cur_cycle] == 0) {
			//printf("Process %d wake up\n", SLEEP.ready[i].PID);
			SLEEP.ready[i].cur_cycle++;
			mov_Prc(&SLEEP, Qlist[SLEEP.ready[i].home], i);
			//show_SLP_list();
			i = 0;
		}
	}
}

void chk_PrcList() {
	if (front == T)	return;
	if (prcList[front].AT == time) {
		//printf("Process %d is inserted..\n", prcList[front].PID);
		printf("   %d", prcList[front].PID);
		enQ(&Q0, prcList[front++]);	// when time = process's AT, put the process into Q0
	}
}
void tick() {
	time++;
	chk_PrcList();	// check waiting list
	check_SLP();	// check IO burst is over
}
void IO_burst() {
	int k;
	for (k = 0; k < SLEEP.top; k++) SLEEP.ready[k].IO_burst[SLEEP.ready[k].cur_cycle]--;
}


int main() {
	Process tmp, *run;
	int i, j, k, min;
	FILE *fp;

	Q0.TQ = 2;
	Q1.TQ = 6;
	SLEEP.top = Q0.top = Q1.top = Q2.top = 0;
	time = 0;
	//input process info
	{
		fp = fopen("input.txt", "rt");
		if (fp == NULL) {
			printf("file open error\n");
			return 0;
		}
		fscanf(fp, "%d", &T);
		printf("Test case: %d\n", T);
		for (i = 0; i < T; i++) {
			tmp.time_T = tmp.total_B = 0;
			fscanf(fp, "%d", &tmp.PID);
			fscanf(fp, "%d", &tmp.AT);
			fscanf(fp, "%d", &tmp.Cycle);
			for (j = 0; j < tmp.Cycle; j++) {
				fscanf(fp, "%d", &tmp.CPU_burst[j]);
				tmp.total_B += tmp.CPU_burst[j];
				if (j < tmp.Cycle - 1) fscanf(fp, "%d", &tmp.IO_burst[j]);
			}
			tmp.cur_cycle = 0;
			prcList[i] = tmp;
		}
		printf("===Prc List===\nPID\tAT\tCycle\tBurst\n");
		for (i = 0; i < T; i++) {
			printf("%d\t", prcList[i].PID);
			printf("%d\t", prcList[i].AT);
			printf("%d\t", prcList[i].Cycle);
			for (j = 0; j < prcList[i].Cycle; j++) {
				printf("%d\t", prcList[i].CPU_burst[j]);
				if (j < prcList[i].Cycle - 1) printf("%d\t", prcList[i].IO_burst[j]);
			}
			printf("\n");
		}
	}	// input process info
	
	printf("INSERT\tTIME\tPREEM\tASLEEP\tTERMINATED\n");
	chk_PrcList();
	printf("\t||%d||\t\n", time);

	while (1) {		
		if (isEmpty(&Q0) == 1) {
			//printf("\tTIME-%d\tQ0 is empty. Scheduling on Q1\n", time);
			// Q1 RR scheduling
			if (isEmpty(&Q1) == 1) {
				//printf("\tTIME-%d\tQ1 is empty. Scheduling on Q2\n", time);
				// Q2 SRTN scheduling
				if (isEmpty(&Q2) == 1) {
					if (isEmpty(&SLEEP) == 1) {
						printf("All Process running is terminated.\n");
						printf("PID\tTT\tWT\tTERM\ttotal\n");
						float tot_TT = 0;
						float tot_WT = 0;
						for (i = 0; i < T; i++) {
							int TT = prcList[i].time_T - prcList[i].AT;
							int WT = TT - prcList[i].total_B;
							tot_TT += TT;
							tot_WT += WT;
							printf("%d\t%d\t%d\t%d\t%d\n", prcList[i].PID, TT, WT, prcList[i].time_T, prcList[i].total_B);
						}
						printf("Avg TT: %.1f\tAvg WT: %.1f\n", tot_TT / T, tot_WT / T);
						break;
					}
					IO_burst();
					tick();
					printf("\t||%d||\t\n", time);
					continue;
				}
				k = 0;
				min = Q2.ready[0].CPU_burst[Q2.ready[0].cur_cycle];
				for (j = 0; j < Q2.top; j++) {
					if (Q2.ready[j].CPU_burst[Q2.ready[j].cur_cycle] < min) {
						k = j;
						min = Q2.ready[j].CPU_burst[Q2.ready[j].cur_cycle];
					}
				}
				run = &Q2.ready[k]; // run is running process
#if _DEBUG
				printf("Q2\t");
				//show_PrcInfo(run);
#endif				
				run->CPU_burst[run->cur_cycle]--;
				IO_burst();
				tick();
				printf("\t||%d||\t", time);
				if (run->CPU_burst[run->cur_cycle] == 0) {
					if (run->cur_cycle == run->Cycle - 1) {
						//printf("TIME-%d\tProcess %d is terminated\n", time, run->PID);
						printf("\t\t   %d\n", run->PID);
						prcList[run->PID - 1].time_T = time;
						deQ(&Q2, k);
						continue;
					}
					else {
						//printf("Process %d is asleep\n", run->PID);
						run->home = 1;
						mov_Prc(&Q2, &SLEEP, k);
						printf("\t   %d\n", run->PID);
						continue;
					}
				}
				printf("\n");
				continue;
				// end Q2 scheduling
			}
			run = &Q1.ready[0]; // run is running process
			for (j = 0; j < Q1.TQ; j++) {
#if _DEBUG
				printf("Q1\t");
				//show_PrcInfo(run);
#endif
				run->CPU_burst[run->cur_cycle]--;
				IO_burst();
				tick();
				printf("\t||%d||\t", time);

				if (run->CPU_burst[run->cur_cycle] == 0) {
					if (run->cur_cycle == run->Cycle - 1) {
						//printf("TIME-%d\tProcess %d is terminated\n", time, run->PID);
						printf("\t\t   %d\n", run->PID);
						prcList[run->PID - 1].time_T = time;
						deQ(&Q1, 0);
						break;
					}
					else {
						//printf("Process %d is asleep\n", run->PID);
						printf("\t   %d\n", run->PID);
						run->home = 0;
						mov_Prc(&Q1, &SLEEP, 0);
						break;
					}
				}
				if (j == Q1.TQ - 1) {
#if _DEBUG
					printf("Process %d is preemted\n", run->PID);
#endif
					printf("   %d", run->PID);
					mov_Prc(&Q1, &Q2, 0);	// preemption from Q1 to Q2
				}
				printf("\n");
			}
			continue;
		}		// end Q1 scheduling

		run = &Q0.ready[0]; // run is running process
		for (j = 0; j < Q0.TQ; j++) {
#if _DEBUG
			printf("Q0\t");
			//show_PrcInfo(run);
#endif
			run->CPU_burst[run->cur_cycle]--;
			IO_burst();
			tick();
			printf("\t||%d||\t", time);
			if (run->CPU_burst[run->cur_cycle] == 0) {
				if (run->cur_cycle == run->Cycle - 1) {
					//printf("TIME-%d\tProcess %d is terminated\n", time, run->PID);
					printf("\t\t   %d\n", run->PID);
					prcList[run->PID - 1].time_T = time;
					deQ(&Q0, 0);
					break;
				}
				else {
					//printf("Process %d is asleep\n", run->PID);
					printf("\t   %d\n", run->PID);
					run->home = 0;
					mov_Prc(&Q0, &SLEEP, 0);
					break;
				}
			}
			if (j == Q0.TQ-1) { 
#if _DEBUG
				printf("Process %d is preemted", run->PID);
#endif
				printf("   %d", run->PID);
				mov_Prc(&Q0, &Q1, 0);		// preemption from Q0 to Q1
			}
			printf("\n");
		}
	}
	//scanf("%d", &T);
}