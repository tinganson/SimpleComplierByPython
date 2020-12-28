# SimpleComplierByPython

```diff
- 欲執行PLY請輸入：python myacc.py
```

# 語法：
* 冪次運算： base  ^  n
```diff
calc > 2^3
8
```
* 根號運算： num  **  n
```diff
calc > 4**2
2.0
```
* for-loop： for 變數 loop 次數 : ("欲執行的指令運算");
```diff
calc > i=0
calc > for 1 to 3 : i=i+2 ;
calc > i
6
```
* if-else： if ("條件判斷") : "expression"; else :"expression" ;
```diff
calc > i=0
calc > if (i<0) : i=1 ;else : i=2;
calc > i
2
```
* 若輸入四則運算，則會依序列出：(1)lex輸出 (2)執行結果 (3)Three-Address Code
```diff
calc > 2*3-6/2^2
LexToken(NUMBER,2,1,0)
LexToken(TIMES,'*',1,1)
LexToken(NUMBER,3,1,2)
LexToken(MINUS,'-',1,3)
LexToken(NUMBER,6,1,4)
LexToken(DIVIDE,'/',1,5)
LexToken(NUMBER,2,1,6)
LexToken(POW,'^',1,7)
LexToken(NUMBER,2,1,8)
4.5
['^', '2', '2', 't1']
['/', '6', 't1', 't2']
['*', '2', '3', 't3']
['-', 't3', 't2', 't4']
['=', 't4', ' ', 'a']]
```
