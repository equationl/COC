#coding=utf-8

'''
*name:layout_data.py
*author:equationl
*date:2014.06.23
*界面布局数据
'''

#扫描图片界面数据
LAYOUT_READ = '''<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
	xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="fill_parent"
	android:layout_height="fill_parent"
	android:background="#aaffa0"
	android:gravity="center"
	android:orientation="vertical">

	<LinearLayout
		android:layout_width="200px"
		android:layout_height="200px"
		android:background="file:///sdcard/photobg.9.png"
		android:gravity="center">

		<TextView
			android:layout_width="wrap_content"
			android:layout_height="wrap_content"
			android:background="file:///sdcard/coc.png"
			android:layout_marginTop="6px"
			android:layout_marginLeft="6px"
			android:layout_marginRight="6px"
			android:layout_marginBottom="6px"
			android:id="@+id/photo"/>

	</LinearLayout>

	<EditText
		android:layout_height="wrap_content"
		android:ems="10"
		android:layout_width="wrap_content"
      android:hint="输入图片路径，如: /sdcard/coc.png"/>
	<LinearLayout
		android:layout_height="wrap_content"
		android:layout_width="wrap_content"
		android:orientation="horizontal">
		
		<Button
			android:layout_height="wrap_content"
			android:text="读取"
			android:layout_width="wrap_content"
			android:id="@+id/btn_read"/>
		
		<Button
			android:layout_height="wrap_content"
			android:text="返回"
			android:layout_width="wrap_content"
			android:id="@+id/btn_return"/>
		
	</LinearLayout>
</LinearLayout>
'''