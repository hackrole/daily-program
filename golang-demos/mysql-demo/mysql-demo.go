package main

import (
	"database/sql"
	"fmt"
	_ "github.com/GO-SQL-Driver/MySQL"
	//"time"
)

func main() {
	db, err := sql.Open("mysql", "root:root@127.0.0.1/golang_mysql_demo?charset=utf8")
	checkErr(err)

	// 插入数据
	stat := "insert into userinfo (username, departname, created) values (?, ?, ?)"
	stmt, err := db.Prepare(stat)
	checkErr(err)

	res, err := stmt.Exec("hackrole", "研发", "2012-09-20")
	checkErr(err)

	id, err := res.LastInsertId()
	checkErr(err)

	fmt.Println(id)
	// 更新数据
	stmt, err = db.Prepare("update userinfo set username=? where uid=?")
	checkErr(err)

	res2, err2 := stmt.Exec("hackrole-update", id)
	checkErr(err2)

	affect, err := res2.RowsAffected()
	checkErr(err)

	fmt.Println(affect)

	// 查询数据
	rows, err := db.Query("select * from userinfo")
	checkErr(err)

	for rows.Next() {
		var uid int
		var username string
		var departname string
		var created string
		err = rows.Scan(&uid, &username, &departname, &created)
		checkErr(err)
		fmt.Println(uid)
		fmt.Println(username)
		fmt.Println(departname)
		fmt.Println(created)
	}

	// 删除数据
	stmt, err = db.Prepare("delete from userinfo where uid=?")
	checkErr(err)

	res3, err3 := stmt.Exec(id)
	checkErr(err3)

	affect, err = res3.RowsAffected()
	checkErr(err)

	fmt.Println(affect)

	db.Close()
}

func checkErr(err error) {
	if err != nil {
		panic(err)
	}
}
