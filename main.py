# streamlit run main.pyで実行
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'
latest_iteration = st.empty()   # 空で用意
bar = st.progress(0)            # バーを用意
for i in range(100):            # プログレスバー更新
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)
'Done!!'

#列を二列作り、それぞれの列に対して操作出来る
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

# Q&Aに使える
expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の内容')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の内容')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の内容')

# sidebarと入れるだけでサイドバーに表示できる
st.sidebar.write('Interactive Widgets')
text = st.sidebar.text_input('あなたの趣味は？')
condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
'あなたの趣味は、',text,'です。'
'コンディション', condition

option = st.selectbox(
    '好きな数字は？',
    list(range(1,11))
)
'あなたの好きな数字は', option, 'です。'

if st.checkbox('Show Image'):
    img = Image.open('mugi.jpg')
    st.image(img, caption='My Cat', use_column_width=True)

st.write('Data Frame')

if st.checkbox('Show Graph'):
    df2 = pd.DataFrame(
        np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],  #乱数を50で割って値を小さくし、新宿の緯度と経度を足した。
        columns=['lat','lon']
    )
    #st.table(df2.style.highlight_max(axis=0)) # 静的な表
    #st.bar_chart(df2)
    st.map(df2)

if st.checkbox('Show Table'):
    df = pd.DataFrame({
        '1列目': [1, 2, 3, 4],
        '2列目': [10, 20, 30, 40]
    })
    #st.write(df)
    #st.dataframe(df.style.highlight_max(axis=0)) # 引数でサイズを指定できる。axisは0が行、1が列。
    st.table(df.style.highlight_max(axis=0)) # 静的な表

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""