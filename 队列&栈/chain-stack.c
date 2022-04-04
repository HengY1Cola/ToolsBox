#include<stdio.h>
#include<malloc.h>
#include<string.h>
#include<stdlib.h>
#define ERROR -1
typedef int SDataType;
typedef struct StackNode
{
	SDataType Data;
	struct StackNode* Next;
}Node, * PNode;//PNode为StackNode的指针
typedef struct Stack
{
	PNode top;
	int count;
}Stack;//指向第一个
struct StackNode* BuyStackNode() {
	struct StackNode* p;
	p = (StackNode*)malloc(sizeof(struct StackNode));
	p->Next = NULL;
	return p;
}//建立一个新的节点
void InitStack(Stack* s){
	s->top= (PNode)malloc(sizeof(StackNode));
	Stack*base=s;//得到最开始的指针和0个个数
	if (!s->top)
		exit(ERROR);
	s->top = NULL;
	s->count = 0;
}//栈的初始化
void PushStack(Stack* s, SDataType e) {
	PNode PNewNode = BuyStackNode();
	PNewNode->Data = e;
	PNewNode->Next = s->top;
	s->top = PNewNode;
	s->count++;
	printf("输入的是%d\n", e);
}//入栈
void PopStack(Stack* s) {
	PNode p;
	SDataType e;
	if (s->top == NULL)exit(ERROR);
	e = s->top->Data;
	printf("删除%d\n", e);
	p = s->top;
	s->top = s->top->Next;
	free(p);
	s->count--;
}//出栈
void PrintCount(Stack* s){
	printf("%d个数\n", s->count);
}//输出长度
void ClearStack(Stack* s) {
	PNode p;
	while (s->top != NULL) {
		p = s->top;
		s->top = s->top->Next;
		free(p);
	}
	s->count = 0;
	printf("已经清空栈表\n");
}//清空栈表
void GetTop(Stack* s, SDataType* e)
{
	if (s->top!= NULL)
	{
		*e = s->top->Data;
	}
	else
		exit(ERROR);
}//获顶
void PrintStack(Stack*s)
{
		PNode p;
		p = s->top;
		while (p)
		{
			printf("%d\n",p->Data);
			p = p->Next;
		}
		if (p == NULL)
			printf("啥都没有了\n");
}//输出
int main() {
	Stack s;
	InitStack(&s);
	PushStack(&s, 1);
	PushStack(&s, 2);
	PushStack(&s, 3);
	PushStack(&s, 4);
	PopStack(&s);
	PrintCount(&s);
	PrintStack(&s);
	ClearStack(&s);
	PrintStack(&s);
	system("pause");
}