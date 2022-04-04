#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <string.h>
typedef int SDataType;
typedef char SDataName;
typedef struct SListNode
{
	SDataType Num;
	SDataName Name[6];
	SDataType Chinese;
	SDataType Math;
	SDataType English;
	struct SListNode* _PNext;
}Node, * PNode;
typedef struct SList
{
	PNode _pHead;//指向链表第一个节点
}SList;
struct SListNode* BuySListNode(SDataType Num, SDataName Name[5], SDataType Chinese, SDataType Math, SDataType English) {
	struct SListNode* p;
	p = (SListNode*)malloc(sizeof(struct SListNode));
	if (!p)
		exit(1);
	p->Num = Num;
	strcpy_s(p->Name, Name);
	p->Chinese = Chinese;
	p->Math = Math;
	p->English = English;
	p->_PNext = NULL;
	return p;
}//获取新的一个节点
void SListInit(SList* s) {
	assert(s);
	s->_pHead = NULL;
}//链表初始化
void SListPushBack(SList* s, SDataType Num, SDataName Name[5], SDataType Chinese, SDataType Math, SDataType English) {
	//找链表最后一个节点
	assert(s);
	PNode pNewNode = BuySListNode(Num, Name, Chinese, Math, English);
	if (s->_pHead == NULL) {//链表没有节点的情况
		s->_pHead = pNewNode;
	}
	else {
		PNode pCur = s->_pHead;
		while (pCur->_PNext) {
			pCur = pCur->_PNext;
		}
		//让最后一个节点指向新节点
		pCur->_PNext = pNewNode;
	}
}//尾插
void SListPrint(SList* s) {             //打印链表
	assert(s);
	PNode pCur = s->_pHead;
	while (pCur) {
		printf("Num is %d,Name is %s,Chinese: %d,Math: %d,English: %d,Aver: %.2f\n", pCur->Num, pCur->Name, pCur->Chinese, pCur->Math, pCur->English, (float)(pCur->Chinese + pCur->Math + pCur->English) / 3);
		pCur = pCur->_PNext;
	}
	printf("\n");
}
void SListInsert(PNode pos, SDataType Num, SDataName Name[5], SDataType Chinese, SDataType Math, SDataType English) {
	PNode pNewNode = NULL;
	if (pos == NULL) {
		return;
	}
	pNewNode = BuySListNode(Num, Name, Chinese, Math, English);

	pNewNode->_PNext = pos->_PNext;
	pos->_PNext = pNewNode;
}//插入
PNode SListFind(SList* s, SDataType Num) {
	assert(s);
	PNode pCur = s->_pHead;
	while (pCur) {
		if (pCur->Num == Num) {
			return pCur;
		}
		pCur = pCur->_PNext;
	}
	return NULL;
}//查找
void SListPrintNode(SList* s, PNode pos) {
	assert(s);
	if (pos) {
		printf("Num is %d,Name is %s,Chinese: %d,Math: %d,English: %d,Aver: %d\n", pos->Num, pos->Name, pos->Chinese, pos->Math, pos->English, (pos->Chinese + pos->Math + pos->English) / 3);
	}
	printf("\n");
}//查找后并单独输出
void SListErase(SList* s, PNode pos) {
	assert(s);
	if (pos == NULL || s->_pHead == NULL) {
		return;
	}
	if (pos == s->_pHead) {
		s->_pHead = pos->_PNext;
	}
	else {
		PNode pPrePos = s->_pHead;
		while (pPrePos && pPrePos->_PNext != pos) {
			pPrePos = pPrePos->_PNext;
		}
		if (pPrePos)
			pPrePos->_PNext = pos->_PNext;
	}
	free(pos);
}//删除给定pos位置的节点。
int main() {
	SList s;
	SListInit(&s);
	SDataName tmp1[6] = "huang";
	SDataName tmp2[6] = "li";
	SDataName tmp3[6] = "luo";
	SDataName tmp4[6] = "yang";
	SListPushBack(&s, 001, tmp1, 88, 87, 87);
	SListPushBack(&s, 002, tmp2, 95, 92, 86);
	SListPushBack(&s, 003, tmp3, 89, 82, 83);
	SListPrint(&s);
	SListInsert(SListFind(&s, 002), 004, tmp4, 87, 93, 86);
	SListPrint(&s);
	SListErase(&s, SListFind(&s, 003));
	SListPrint(&s);
	SListPrintNode(&s, SListFind(&s, 002));
	system("pause");
}