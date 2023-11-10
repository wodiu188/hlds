package com.axshare.entity;

import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

import java.util.Date;


@TableName
@Data
public class Student {
    @TableField
    private int id;
    @TableField
    private String studentname;
    @TableField
    private String sex;
    @TableField
    private int classname;
    @TableField
    private Date createtime;
    @TableField
    private Date modifytime;

}
