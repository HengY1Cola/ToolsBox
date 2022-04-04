#include<stdio.h>
#include<stdlib.h>
#define TRUE  1
#define FALSE 0
#define OK 1
#define ERROR 0
#define INFEASIBLE  -1
#define OVERFLOW  -2
//说明Status函数的返回值是这6种类型的数
#define NULL 0
typedef int Status;
typedef float ElemType;
typedef ElemType* Triplet;
Status InitTriplet(Triplet& T, ElemType v1, ElemType v2, ElemType v3) {
	T = (ElemType*)malloc(3 * sizeof(ElemType));
	if (!T)exit(OVERFLOW);
	T[0] = v1;
	T[1] = v2;
	T[2] = v3;
	return OK;
}//分配储存空间
Status DestoryTriplet(Triplet& T) {
	free(T);
	T = NULL;
	return OK;
}//销毁
Status Get(Triplet T, int i, ElemType& e) {
	if (i < 1 || i>3)return ERROR;
	e = T[i - 1];
	return OK;
}//读取
Status Put(Triplet& T, int i, ElemType& e) {
	if (i < 1 || i>3)return ERROR;
	T[i - 1] = e;
	return OK;
}//存入
Status Max(Triplet T, ElemType& e) {
	e = (T[0] >= T[1]) ? ((T[0] >= T[2]) ? T[0] : T[2]) : ((T[1] >= T[2]) ? T[1] : T[2]);
	return e;
}//求最大值
int main() {
	char ch;
	float v1, v2, v3;
	printf("请输入3个数\n");
	scanf_s("%f,%f,%f", &v1, &v2, &v3);
	Triplet T;
	InitTriplet(T, v1, v2, v3);
	printf("请选择:\n");
	printf("a是销毁\n");
	printf("b是更改第几个数\n");
	printf("c是读取第几个数\n");
	printf("d是求最大值\n");
	printf("按q键退出\n");
	//按q键退出
	while ((ch = getchar()) != 'q') {
		if (ch == 'a') {
			DestoryTriplet(T);
			break;
		}//销毁
		else if (ch == 'b') {
			int i;
			float e;
			printf("请输入想更改第几个数");
			scanf_s("%d", &i);
			if (i >= 1 && i <= 3) {
				printf("请输入想更改的值");
				scanf_s("%f", &e);
				Put(T, i, e);
				printf("请继续选择\n");
			}
			else {
				printf("错误，请继续选择");
				continue;
			}
		}//存入
		else if (ch == 'c') {
			int i;
			float e;
			printf("想读取第几个数？");
			scanf_s("%d", &i);
			if (i >= 1 && i <= 3) {
				Get(T, i, e);
				printf("该数是：%.2f\n", e);
				printf("请继续选择\n");
			}
			else {
				printf("错误，请继续选择");
				continue;
			}

		}//读取
		else if (ch == 'd') {
			float e;
			e = Max(T, e);
			printf("最大值是%.2f\n", e);
		}//求最大值
		else if (ch != 'a' && ch != 'b' && ch != 'c' && ch != 'd' && ch != '\n') {
			printf("错误");
			continue;
		}
	}
	return 0;
}












