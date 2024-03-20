'''
表: Employees

+-------------+---------+
| 列名        | 类型     |
+-------------+---------+
| employee_id | int     |
| name        | varchar |
| salary      | int     |
+-------------+---------+
employee_id 是这个表的主键(具有唯一值的列)。
此表的每一行给出了雇员id ，名字和薪水。
 

编写解决方案，计算每个雇员的奖金。
如果一个雇员的 id 是 奇数 并且他的名字不是以 'M' 开头，那么他的奖金是他工资的 100% ，否则奖金为 0 。

返回的结果按照 employee_id 排序。

返回结果格式如下面的例子所示。

 

示例 1:

输入：
Employees 表:
+-------------+---------+--------+
| employee_id | name    | salary |
+-------------+---------+--------+
| 2           | Meir    | 3000   |
| 3           | Michael | 3800   |
| 7           | Addilyn | 7400   |
| 8           | Juan    | 6100   |
| 9           | Kannon  | 7700   |
+-------------+---------+--------+
输出：
+-------------+-------+
| employee_id | bonus |
+-------------+-------+
| 2           | 0     |
| 3           | 0     |
| 7           | 7400  |
| 8           | 0     |
| 9           | 7700  |
+-------------+-------+
解释：
因为雇员id是偶数，所以雇员id 是2和8的两个雇员得到的奖金是0。
雇员id为3的因为他的名字以'M'开头，所以，奖金是0。
其他的雇员得到了百分之百的奖金。
'''
import pandas as pd

columns = ['employee_id', 'name', 'salary']
data = [[2, 'Meir', 3000], [3, 'Michael', 3800], [
    7, 'Addilyn', 7400], [8, 'Juan', 6100], [9, 'Kannon', 7700]]
employees = pd.DataFrame(data, columns=columns)


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    df1 = employees[(employees['employee_id'] % 2 == 1) & ~(
        employees['name'].str.startswith('M'))][['employee_id', 'salary']]

    df2 = employees[~(employees['employee_id'] % 2 == 1) | (
        employees['name'].str.startswith('M'))][['employee_id', 'salary']]
    df2['salary'] = 0

    df2 = pd.concat([df1, df2]).sort_values('employee_id')
    df2.columns = ['employee_id', 'bonus']
    return df2


print(calculate_special_bonus(employees))
