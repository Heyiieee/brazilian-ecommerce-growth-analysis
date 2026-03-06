import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
MACARON_COLORS = ['#FF9EB5', '#7EC8E3','#6ECB6E', '#C7B8EA','#FFC8A2','#F9E076','#87CEEB', '#FFA07A' ]


df_main = pd.read_excel('D:\Desktop\数分项目\巴西电商数据分析\结果\无标题_20260305.xls', sheet_name='Sheet1')
df1 = df_main[['month', 'orders', 'avg_order_value', 'users']].copy()

# 新老客数据表
df_newold = pd.read_excel('D:\Desktop\数分项目\巴西电商数据分析\结果\新老客数据.xls', sheet_name='Sheet1')

# GMV数据表（CSV无表头）
df_gmv = pd.read_csv('D:\Desktop\数分项目\巴西电商数据分析\结果\GMV结果.csv', header=None, names=['month', 'gmv'], encoding='utf-8')

# 2. 将月份统一转换为日期类型并排序
for df in [df1, df_newold, df_gmv]:
    df['month'] = pd.to_datetime(df['month'], format='%Y-%m')
    df.sort_values('month', inplace=True)


# ---------- 图1：GMV趋势图 ----------
plt.figure(figsize=(10, 6))
plt.plot(df_gmv['month'], df_gmv['gmv'], marker='o', linestyle='-',
         color=MACARON_COLORS[0], linewidth=2, markersize=6)
plt.title('GMV趋势图', fontsize=14)
plt.xlabel('月份', fontsize=12)
plt.ylabel('GMV', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('D:\Desktop\数分项目\巴西电商数据分析\images\gmv_trend.png', dpi=300, bbox_inches='tight')
plt.close()

# ---------- 图2：订单与用户趋势图（双Y轴，订单数面积填充） ----------
fig, ax1 = plt.subplots(figsize=(10, 6))
ax2 = ax1.twinx()

# 订单数：半透明面积填充 + 折线（粗线+标记）
ax1.fill_between(df1['month'], 0, df1['orders'], color=MACARON_COLORS[1], alpha=0.2)
line1, = ax1.plot(df1['month'], df1['orders'], marker='s',
                  color=MACARON_COLORS[1], linewidth=2.5, markersize=6, label='订单数')

# 用户数：折线（稍细，保持清晰）
line2, = ax2.plot(df1['month'], df1['users'], marker='^',
                  color=MACARON_COLORS[2], linewidth=2.0, markersize=5, label='用户数')

ax1.set_xlabel('月份', fontsize=12)
ax1.set_ylabel('订单数', color=MACARON_COLORS[1], fontsize=12)
ax2.set_ylabel('用户数', color=MACARON_COLORS[2], fontsize=12)
ax1.tick_params(axis='x', rotation=45)
ax1.set_title('订单与用户趋势图', fontsize=14)

# 合并图例
lines = [line1, line2]
ax1.legend(lines, [l.get_label() for l in lines], loc='upper left')

# 网格线置于底层
ax1.set_axisbelow(True)
ax2.set_axisbelow(True)
ax1.grid(True, linestyle='--', alpha=0.7)

fig.tight_layout()
fig.savefig('D:\Desktop\数分项目\巴西电商数据分析\images\orders_users_trend.png', dpi=300, bbox_inches='tight')
plt.close(fig)

# ---------- 图3：客单价趋势图 ----------
plt.figure(figsize=(10, 6))
plt.plot(df1['month'], df1['avg_order_value'], marker='d',
         color=MACARON_COLORS[3], linewidth=2, markersize=6)
plt.title('客单价趋势图', fontsize=14)
plt.xlabel('月份', fontsize=12)
plt.ylabel('平均客单价', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('D:\Desktop\数分项目\巴西电商数据分析\images\\avg_order_value_trend.png', dpi=300, bbox_inches='tight')
plt.close()

# ---------- 图4：新客占比趋势图 ----------
plt.figure(figsize=(10, 6))
plt.plot(df_newold['month'], df_newold['new_user_ratio'], marker='o',
         color=MACARON_COLORS[4], linewidth=2, markersize=6)
plt.title('新客占比趋势图', fontsize=14)
plt.xlabel('月份', fontsize=12)
plt.ylabel('新客占比', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('D:\Desktop\数分项目\巴西电商数据分析\images\\new_user_ratio_trend.png', dpi=300, bbox_inches='tight')
plt.close()

# ---------- 图5：新老客数量对比图（堆叠柱状图） ----------
plt.figure(figsize=(10, 6))
x = np.arange(len(df_newold['month']))
width = 0.8
plt.bar(x, df_newold['new_users'], width, label='新客', color=MACARON_COLORS[0])
plt.bar(x, df_newold['returning_users'], width, bottom=df_newold['new_users'],
        label='老客', color=MACARON_COLORS[5])
plt.title('新老客数量对比图', fontsize=14)
plt.xlabel('月份', fontsize=12)
plt.ylabel('用户数', fontsize=12)
plt.xticks(x, df_newold['month'].dt.strftime('%Y-%m'), rotation=45)
plt.legend()
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('D:\Desktop\数分项目\巴西电商数据分析\images\\new_returning_users_comparison.png', dpi=300, bbox_inches='tight')
plt.close()