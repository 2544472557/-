# -
关于numpy库的一些使用
记录关于numpy库的一些使用例如创建二维及以上矩阵
乘除法np.dot(矩阵a，矩阵b)或者使用，矩阵a.dot（矩阵b）
对于想要具体求某列数据和某行，可以采用axis=0表示每一列，axis=1表示每一行
numpy中平均值求法：np.mean/np.average 判断某个最大最小值的索引：avgmax/min 求中位数：median ，进行累加使用cumsum ，累差：diff
找矩阵中的非0元素，采用nonzero，排序采用sort，转置transpose，矩阵的切片clip（矩阵，x：判断小于x的值全部变为x，y：大于y的值全部变为y）
numpy矩阵的合并vstack（矩阵a，矩阵b）：进行上下合并，hstack（矩阵a，矩阵b）：进行左右合并

若要将类似于【1,1,1,1,1】变为竖列，不能够采取矩阵. T进行实现，需要采取矩阵[:,np.newaxis]进行将列变为竖列
多个数组或者矩阵进行合并采用np.concatenate(矩阵a，矩阵b，矩阵c......)
切割数组同合并数组vsplit，hsplit
