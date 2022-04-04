#include<stdio.h>
#include <malloc.h>
#include<stdlib.h>
#define max 50
#define TRUE 1
#define FLASE 0
typedef int ElemType;
typedef int Status;
typedef struct {
	ElemType* elem;
	int length;
	int size;
}list;
Status InitList(list& p, int size) {
	p.elem = (ElemType*)malloc(size * sizeof(ElemType));
	p.length = 0;
	p.size = size;
	return TRUE;
}
void createlist(list& p) {
	int i;
	for (i = 0; i < p.size; i++) {
		scanf_s("%d", &p.elem[i]);
		p.length++;
	}
}//creat
void showlist(list& p) {
	int i;
	printf("\nThese %d datas are:\n", p.length);
	if (p.length <= 0)
	{
		printf("No data!\n");
		return;
	}
	for (i = 0; i < p.length; i++)
		printf(" %d ", p.elem[i]);
	printf("\nlength of the list is:%d ", p.length);
}//show
Status insretlist(list& p, int new_elem, int i) {
	int j;
	if (p.length >= max)//溢出
	{
		printf("the list is full,can not insert.");
		return false;
	}
	if (i<1 || i>p.length + 1)//i是否符合
	{
		printf("\n%d is invalid value", i);
		return false;
	}
	for (j = p.length; j >= i; j--)// 将插入位置之后的元素依次往后移动一个位置
		p.elem[j] = p.elem[j - 1];//从最后一个元素开始移动
	p.elem[i - 1] = new_elem;
	p.length++;
	return TRUE;
}//insert
int delect(list& p, int i) {
	int j;
	if (i<1 || i>p.length) {
		printf("elem not exist");
		return false;
	}
	for (j = i; j <= p.length; j++)
		p.elem[j - 1] = p.elem[j];//从删除元素之后的第一个元素开始依次将后面元素向前移动一个位置
	p.length--;
	return true;
}//delect
int main() {
	list p;
	int size;
	printf("\n顺序表初始化\n");
	printf("请输入顺序表的长度size：\n");
	scanf_s("%d", &size);
	InitList(p, size);
	printf("请创建顺序表");
	createlist(p);
	showlist(p);
	insretlist(p, 9, 3);
	showlist(p);
	delect(p, 3);
	showlist(p);
}







