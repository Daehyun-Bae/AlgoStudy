#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>
using namespace std;
#define MAX_DEPTH 100

vector<int> puzzle;
vector<int> answer = {1, 2, 3, 4, 5, 6, 7, 8, 0};


int moved[MAX_DEPTH];
int solution[MAX_DEPTH];
int steps = MAX_DEPTH;
int open_size = 0;
int visited = 0;

int get_pos(vector<int> vec);
bool is_goal(vector<int> vec);
void print_map(vector<int> map);
bool chk_visited(vector<int> vec);
int index_visited(vector<int> vec);


class node {
	public:
		vector<int> state;
		int depth;
		int pos, parent, cost;
		node() {
			depth = cost = 0;
			pos = parent= -1;
		}
		node(vector<int> vec) {
			state = vec;
			pos = get_pos(vec);
			parent = -1;
		}
		~node() {
			state.clear();
		}
	public:
		bool chk_R() { return !(pos % 3 == 2); }  // check if 0 could move right
		bool chk_L() { return !(pos % 3 == 0); }
		bool chk_D() { return !(pos > 5); }
		bool chk_U() { return !(pos < 3); }

		void move_R() {					// move operation
			parent = pos;
			swap(state[pos], state[pos + 1]);
			pos = pos + 1;
		}
		void move_L() { 
			parent = pos;
			swap(state[pos], state[pos - 1]);
			pos = pos - 1;
		}
		void move_D() { 
			parent = pos;
			swap(state[pos], state[pos + 3]); 
			pos = pos + 3;
		}
		void move_U() { 
			parent = pos;			 
			swap(state[pos], state[pos - 3]); 
			pos = pos - 3;
		}
		int H1() {
			int cost = 0;
			for (int i = 0; i < 9; i++) {
				if ((i + 1) % 9 != state[i]) cost++;	// return # of tiles out of place
			}
			return cost;
		}
		int H2() {
			int cost = 0;
			for (int i = 0; i < 9; i++) {
				cost += (int)abs(state[i] - (i + 1) % 9) / 3 + (int)abs(state[i] - (i + 1) % 9) % 3;
			}
			return cost;		// return manhattan distance
		}
		int get_cost(int n) {
			switch (n) {
			case 1:
				return cost + H1();
			case 2:
				return cost + H2();
			default:
				return 0;
			}
		}
};

vector<node> OPEN, CLOSED;
int get_position(node n, int a);

void dfs() {
	while (1) {
		if (OPEN.empty()) {
			printf("Solution Not found\n");
			return;
		}
		node tmp;
		tmp = OPEN.back();
		visited++;
		if (visited % 10000 == 0) printf("%d nodes are visited...\n", visited);
		CLOSED.push_back(tmp);
		if (is_goal(tmp.state)) {
			printf("DFS Solution found in %d step\n", tmp.depth);
			steps = tmp.depth;
			return;
		}
		else {
			OPEN.pop_back();
			if (tmp.chk_U()) {
				tmp.move_U();
				if (!chk_visited(tmp.state)) {
					tmp.depth++;
					OPEN.push_back(tmp);
					tmp.depth--;
				}
				tmp.move_D();
			}
			if (tmp.chk_L()) {
				tmp.move_L();
				if (!chk_visited(tmp.state)) {
					tmp.depth++;
					OPEN.push_back(tmp);
					tmp.depth--;
				}
				tmp.move_R();
			}
			if (tmp.chk_D()) {
				tmp.move_D();
				if (!chk_visited(tmp.state)) {
					tmp.depth++;
					OPEN.push_back(tmp);
					tmp.depth--;
				}
				tmp.move_U();
			}
			if (tmp.chk_R()) {
				tmp.move_R();
				if (!chk_visited(tmp.state)) {
					tmp.depth++;
					OPEN.push_back(tmp);
					tmp.depth--;
				}
				tmp.move_L();
			}
			if (open_size < OPEN.size()) open_size = OPEN.size();
		}
	}
}
void bfs() {
	while (1) {
		if (OPEN.empty()) {
			printf("Solution Not found\n");
			return;
		}
		node tmp;
		tmp = OPEN.front();
		visited++;
		if (visited % 10000 == 0) printf("%d nodes are visited...\n", visited);
		if (tmp.depth != 0) moved[tmp.depth - 1] = tmp.state[tmp.parent];
		CLOSED.push_back(tmp);
		if (is_goal(tmp.state)) {
			printf("BFS Solution found in %d step\n", tmp.depth);
			steps = tmp.depth;
			for (int i = 0; i < steps; i++) solution[i] = moved[i];
			return;
		}
		else {
			OPEN.erase(OPEN.begin());
			if (tmp.chk_U()) {
				tmp.move_U();
				if (!chk_visited(tmp.state)) {
					tmp.depth++;
					OPEN.push_back(tmp);
					tmp.depth--;
				}
				tmp.move_D();
			}
			if (tmp.chk_L()) {
				tmp.move_L();
				if (!chk_visited(tmp.state)) {
					tmp.depth++;
					OPEN.push_back(tmp);
					tmp.depth--;
				}
				tmp.move_R();
			}
			if (tmp.chk_D()) {
				tmp.move_D();
				if (!chk_visited(tmp.state)) {
					tmp.depth++;
					OPEN.push_back(tmp);
					tmp.depth--;
				}
				tmp.move_U();
			}
			if (tmp.chk_R()) {
				tmp.move_R();
				if (!chk_visited(tmp.state)) {
					tmp.depth++;
					OPEN.push_back(tmp);
					tmp.depth--;
				}
				tmp.move_L();
			}
			if (open_size < OPEN.size()) open_size = OPEN.size();
		}
	}
}
void A1() {
	while (1) {
		if (OPEN.empty()) {
			printf("Solution Not found\n");
			return;
		}
		node tmp;
		tmp = OPEN.front();
		visited++;
		if (visited % 10000 == 0) printf("%d nodes are visited...\n", visited);
		if (tmp.depth != 0) moved[tmp.depth - 1] = tmp.state[tmp.parent];
		CLOSED.push_back(tmp);
		if (is_goal(tmp.state)) {
			printf("A* 1 Solution found in %d step\n", tmp.depth);
			steps = tmp.depth;
			for (int i = 0; i < steps; i++) solution[i] = moved[i];
			return;
		}
		else {
			OPEN.erase(OPEN.begin());
			if (tmp.chk_U()) {
				tmp.move_U();
				if (!chk_visited(tmp.state)) {
					tmp.depth++; tmp.cost++;
					OPEN.insert(OPEN.begin() + get_position(tmp, 1), tmp);
					tmp.depth--; tmp.cost--;
				}
				tmp.move_D();
			}
			if (tmp.chk_L()) {
				tmp.move_L();
				
				if (!chk_visited(tmp.state)) {
					tmp.depth++; tmp.cost++;
					OPEN.insert(OPEN.begin() + get_position(tmp, 1), tmp);
					tmp.depth--; tmp.cost--;
				}
				tmp.move_R();
			}
			if (tmp.chk_D()) {
				tmp.move_D();
				if (!chk_visited(tmp.state)) {
					tmp.depth++; tmp.cost++;
					OPEN.insert(OPEN.begin() + get_position(tmp, 1), tmp);
					tmp.depth--; tmp.cost--;
				}
				tmp.move_U();
			}
			if (tmp.chk_R()) {
				tmp.move_R();
				if (!chk_visited(tmp.state)) {
					tmp.depth++; tmp.cost++;
					OPEN.insert(OPEN.begin() + get_position(tmp, 1), tmp);
					tmp.depth--; tmp.cost--;
				}
				tmp.move_L();
			}
			if (open_size < OPEN.size()) open_size = OPEN.size();
		}
	}
}
void A2() {
	while (1) {
		if (OPEN.empty()) {
			printf("Solution Not found\n");
			return;
		}
		node tmp;
		tmp = OPEN.front();
		visited++;
		if (visited % 10000 == 0) printf("%d nodes are visited...\n", visited);
		if (tmp.depth != 0) moved[tmp.depth - 1] = tmp.state[tmp.parent];
		CLOSED.push_back(tmp);
		if (is_goal(tmp.state)) {
			printf("A* 2 Solution found in %d step\n", tmp.depth);
			steps = tmp.depth;
			for (int i = 0; i < steps; i++) solution[i] = moved[i];
			return;
		}
		else {
			OPEN.erase(OPEN.begin());
			if (tmp.chk_U()) {
				tmp.move_U();
				if (!chk_visited(tmp.state)) {
					tmp.depth++; tmp.cost++;
					OPEN.insert(OPEN.begin() + get_position(tmp, 2), tmp);
					tmp.depth--; tmp.cost--;
				}
				tmp.move_D();
			}
			if (tmp.chk_L()) {
				tmp.move_L();

				if (!chk_visited(tmp.state)) {
					tmp.depth++; tmp.cost++;
					OPEN.insert(OPEN.begin() + get_position(tmp, 2), tmp);
					tmp.depth--; tmp.cost--;
				}
				tmp.move_R();
			}
			if (tmp.chk_D()) {
				tmp.move_D();
				if (!chk_visited(tmp.state)) {
					tmp.depth++; tmp.cost++;
					OPEN.insert(OPEN.begin() + get_position(tmp, 2), tmp);
					tmp.depth--; tmp.cost--;
				}
				tmp.move_U();
			}
			if (tmp.chk_R()) {
				tmp.move_R();
				if (!chk_visited(tmp.state)) {
					tmp.depth++; tmp.cost++;
					OPEN.insert(OPEN.begin() + get_position(tmp, 2), tmp);
					tmp.depth--; tmp.cost--;
				}
				tmp.move_L();
			}
			if (open_size < OPEN.size()) open_size = OPEN.size();
		}
	}
}
void ida1() {
	int max_cost;
	int cur_cost;
	node root;
	root = OPEN.back();
	max_cost = root.H1();

	while (1) {
		while (1) {
			if (OPEN.empty()) break;
			node tmp;
			tmp = OPEN.back();
			cur_cost = tmp.cost + tmp.H1();
			OPEN.pop_back();
			if (cur_cost <= max_cost) {
				visited++;
				if (visited % 10000 == 0) printf("%d nodes are visited...\n", visited);
				if (tmp.depth != 0) moved[tmp.depth - 1] = tmp.state[tmp.parent];
				CLOSED.push_back(tmp);
				if (is_goal(tmp.state)) {
					printf("IDA 1 Solution found in %d step\n", tmp.depth);
					steps = tmp.depth;
					for (int i = 0; i < steps; i++) solution[i] = moved[i];
					return;
				}
				else {
					if (tmp.chk_U()) {
						tmp.move_U();
						if (!chk_visited(tmp.state)) {
							tmp.depth++; tmp.cost++;
							OPEN.push_back(tmp);
							tmp.depth--; tmp.cost--;
						}
						tmp.move_D();
					}
					if (tmp.chk_L()) {
						tmp.move_L();
						if (!chk_visited(tmp.state)) {
							tmp.depth++; tmp.cost++;
							OPEN.push_back(tmp);
							tmp.depth--; tmp.cost--;
						}
						tmp.move_R();
					}
					if (tmp.chk_D()) {
						tmp.move_D();
						if (!chk_visited(tmp.state)) {
							tmp.depth++; tmp.cost++;
							OPEN.push_back(tmp);
							tmp.depth--; tmp.cost--;
						}
						tmp.move_U();
					}
					if (tmp.chk_R()) {
						tmp.move_R();
						if (!chk_visited(tmp.state)) {
							tmp.depth++; tmp.cost++;
							OPEN.push_back(tmp);
							tmp.depth--; tmp.cost--;
						}
						tmp.move_L();
					}
					if (open_size < OPEN.size()) open_size = OPEN.size();
				}
			}	// end if
		}
		max_cost++;
		CLOSED.clear();
		OPEN.push_back(root);
	}
}
void ida2() {
	int max_cost;
	int cur_cost;
	node root;
	root = OPEN.back();
	max_cost = root.H2();

	while (1) {
		while (1) {
			if (OPEN.empty()) break;
			node tmp;
			tmp = OPEN.back();
			cur_cost = tmp.cost + tmp.H2();
			OPEN.pop_back();
			if (cur_cost <= max_cost) {
				visited++;
				if (visited % 10000 == 0) printf("%d nodes are visited...\n", visited);
				if (tmp.depth != 0) moved[tmp.depth - 1] = tmp.state[tmp.parent];
				CLOSED.push_back(tmp);
				if (is_goal(tmp.state)) {
					printf("IDA 2 Solution found in %d step\n", tmp.depth);
					steps = tmp.depth;
					for (int i = 0; i < steps; i++) solution[i] = moved[i];
					return;
				}
				else {
					if (tmp.chk_U()) {
						tmp.move_U();
						if (!chk_visited(tmp.state)) {
							tmp.depth++; tmp.cost++;
							OPEN.push_back(tmp);
							tmp.depth--; tmp.cost--;
						}
						tmp.move_D();
					}
					if (tmp.chk_L()) {
						tmp.move_L();
						if (!chk_visited(tmp.state)) {
							tmp.depth++; tmp.cost++;
							OPEN.push_back(tmp);
							tmp.depth--; tmp.cost--;
						}
						tmp.move_R();
					}
					if (tmp.chk_D()) {
						tmp.move_D();
						if (!chk_visited(tmp.state)) {
							tmp.depth++; tmp.cost++;
							OPEN.push_back(tmp);
							tmp.depth--; tmp.cost--;
						}
						tmp.move_U();
					}
					if (tmp.chk_R()) {
						tmp.move_R();
						if (!chk_visited(tmp.state)) {
							tmp.depth++; tmp.cost++;
							OPEN.push_back(tmp);
							tmp.depth--; tmp.cost--;
						}
						tmp.move_L();
					}
					if (open_size < OPEN.size()) open_size = OPEN.size();
				}
			}	// if end
		}
		max_cost++;
		CLOSED.clear();
		OPEN.push_back(root);
	}
}

int main() {
	int a;
	int n = 1;
	while (n == 1) {
		printf("1.DFS 2.BFS 3.A1 4.A2 5.IDA1 6.IDA2\n");
		cin >> a;
		printf("Type puzzle\n");
		for (int i = 0; i < 9; i++) {		// input the puzzle
			cin >> n;
			puzzle.push_back(n);
		}
		node N(puzzle);
		OPEN.push_back(N);
		switch (a) {
		case 1:
			dfs();
			break;
		case 2:
			bfs();
			printf("==Solution==\n");
			for (a = 0; a < steps; a++) {
				printf("[%d] step: %d\n", a, solution[a]);
			}
			break;
		case 5:
			ida1();
			printf("==Solution==\n");
			for (a = 0; a < steps; a++) {
				printf("[%d] step: %d\n", a, solution[a]);
			}
			break;
		case 6:
			ida2();
			printf("==Solution==\n");
			for (a = 0; a < steps; a++) {
				printf("[%d] step: %d\n", a, solution[a]);
			}
			break;
		case 3:
			A1();
			printf("==Solution==\n");
			for (a = 0; a < steps; a++) {
				printf("[%d] step: %d\n", a, solution[a]);
			}
		case 4:
			A2();
			printf("==Solution==\n");
			for (a = 0; a < steps; a++) {
				printf("[%d] step: %d\n", a, solution[a]);
			}
			break;
		default:
			break;
		}
		printf("The total number of visited node: %d\n", visited);
		printf("Maximun OPEN list size: %d\n", open_size);
		OPEN.clear();
		CLOSED.clear();
		puzzle.clear();
		open_size = 0; visited = 0;
		printf("Countinue?(yes = 1)\n");
		cin >> n;
	}
}


int get_pos(vector<int> vec) {
	for (unsigned int i = 0; i < vec.size(); i++)
		if (vec[i] == 0) return i;		// get index of 0
}
bool is_goal(vector<int> vec) {
	for (unsigned int i = 0; i < vec.size(); i++) {
		if (vec[i] != (i + 1) % 9)
			return false;
	}
	return true;
}
void print_map(vector<int> map) {			// using for debugging
	printf("======================\n");
	for (unsigned int i = 0; i < map.size(); i++) {
		cout << map[i];
		if (i % 3 == 2) cout << endl;
	}
	printf("======================\n");
}
bool chk_visited(vector<int> vec) {				// check v is already visited
	int i, j, count = 0;
	for (i = 0; i < CLOSED.size(); i++) {
		for (j = 0; j < 9; j++) {
			if (vec[j] != CLOSED[i].state[j]) {
				count--;
				break;
			}
		}
		if (j == 9) {
			return true;
		}
		count++;
	}
	return false;
}
int index_visited(vector<int> vec) {				// check v is already visited
	int i, j, count = 0;
	for (i = 0; i < CLOSED.size(); i++) {
		for (j = 0; j < 9; j++) {
			if (vec[j] != CLOSED[i].state[j]) {
				count--;
				break;
			}
		}
		if (j == 9) {
			return i;
		}
		count++;
	}
	return -1;
}
int get_position(node n, int a) {
	if (OPEN.empty()) return 0;
	int i, cost = n.get_cost(a);
	for (i = 0; i < OPEN.size(); i++) {
		if (cost <= OPEN[i].get_cost(a)) return i;
	}
	return OPEN.size();
}