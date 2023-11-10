package com.axshare.entity;

import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

@TableName
@Data
public class Class {
    @TableField
    private int id;
    @TableField
    private String classname;
    @TableField
    private int studentid;

}
