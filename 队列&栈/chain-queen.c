#include<stdio.h>
#include<malloc.h>
#include<string.h>
#include<stdlib.h>
#define ERROR -1
typedef int SDataType;
typedef struct QueueNode
{
	SDataType Data;
	struct  QueueNode* Next;
}Node, * PNode;//PNode为StackNode的指针
typedef struct {
	Node* front;
	Node* rear;
}LinkQueue;
struct  QueueNode* BuyQueueNode() {
	struct  QueueNode* p;
	p = (QueueNode*)malloc(sizeof(struct  QueueNode));
	p->Next = NULL;
	return p;
}//建立一个新的节点
void InitQueue(LinkQueue* s) {
	s->front= s->rear = NULL;
}//队的初始化
int QueueEmpty(LinkQueue* s){
	return(s->front == NULL && s->rear == NULL);
}
void EnQueue(LinkQueue* s, SDataType e) {
	PNode PNewNode = BuyQueueNode();
	PNewNode->Data = e;
	PNewNode->Next = NULL;
	if (QueueEmpty(s)) {
		s->front= s->rear= PNewNode;
		s->rear = PNewNode;
	}
	else {
		s->rear->Next = PNewNode;
		s->rear = PNewNode;
	}
}//入队
void DeQueue(LinkQueue* s)
{
	if (QueueEmpty(s))     //判断队列是否为空
		printf("Error,the linkqueue is empty!");
	PNode a = s->front;
	printf("删除的是%d\n", a->Data);
	if (s->front == s->rear)   //判断队列是否只有一个节点
		s->front = s->rear = NULL;
	else
		s->front= a->Next;
	free(a);
	
}//出队
void ReadQueue(LinkQueue* s)
{
	if (QueueEmpty(s))     //判断队列是否为空
		printf("Error,the linkqueue is empty!");
	else {
		PNode a = s->front;
		while (a!= NULL) {
			printf("%d\n", a->Data);
			a = a->Next;
		}
	}
}
int main() {
	int a;
	LinkQueue s;
	InitQueue(&s);
	EnQueue(&s, 4);
	EnQueue(&s, 5);
	EnQueue(&s, 7);
	EnQueue(&s, 6);
	EnQueue(&s, 8);
	ReadQueue(&s);
	DeQueue(&s);
	DeQueue(&s);
	ReadQueue(&s);
}