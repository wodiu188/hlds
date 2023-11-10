package com.axshare.entity;

import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

import java.util.Date;

@TableName
@Data
public class Subject {
    @TableField
    private int id;
    @TableField
    private String subjectname;
    @TableField
    private int score;
    @TableField
    private int studentid;
    @TableField
    private Date createtime;
    @TableField
    private Date modifytime;
}
