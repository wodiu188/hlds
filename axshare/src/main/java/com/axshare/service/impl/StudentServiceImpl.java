package com.axshare.service.impl;

import com.axshare.entity.Student;
import com.axshare.mapper.StudentMapper;
import com.axshare.service.StudentService;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import org.springframework.stereotype.Service;

/**
 * <p>
 *  服务实现类
 * </p>
 *
 * @author wodiu
 * @since 2023-11-10 02:23:50
 */
@Service
public class StudentServiceImpl extends ServiceImpl<StudentMapper, Student> implements StudentService {

}
