#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>
#define maxsize 30

typedef struct node
{
    int* base;
    int* top;
    int stacksize;
}Stack;
void InitStack(Stack* S)
{
    S->base = (int*)malloc(sizeof(int) * maxsize);//给栈分配数组空间
    if (!S->base)//判断没有开拓新空间
        exit(0);
    S->top = S->base;
    S->stacksize = maxsize;
}//初始化栈
void PushStack(Stack* S, int elem)
{

    *S->top = elem;//先入
    S->top = S->top + 1;//往上移一个

}//入栈
int PopStack(Stack* S)
{
    int elem;
    S->top = S->top - 1;
    elem = *S->top; //栈顶指针先减一，再将栈顶元素出栈
    return elem;
}//出栈
void PrintStack(Stack* S)
{
    if (S->base == S->top) {
        printf("栈为空！");
    }

    int* p;

    p = S->top;

    printf("输出栈中所有数据：\n");

    while (p > S->base) {
        p--;
        printf("%d\n", *p);//*p表示p指向的变量值
    }
}//输出
int main() {
    Stack s;
    InitStack(&s);
    PushStack(&s, 4);
    PushStack(&s, 5);
    PushStack(&s, 9);
    PushStack(&s, 8);
    PrintStack(&s);
    PopStack(&s);
    PopStack(&s);
    PrintStack(&s);
}