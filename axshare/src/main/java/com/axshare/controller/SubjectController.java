package com.axshare.controller;

import com.axshare.entity.Student;
import com.axshare.entity.Subject;
import com.axshare.mapper.StudentMapper;
import com.axshare.mapper.SubjectMapper;
import com.axshare.utils.R;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.Date;
import java.util.HashMap;
import java.util.List;

/**
 * <p>
 *  前端控制器
 * </p>
 *
 * @author wodiu
 * @since 2023-11-10 02:25:05
 */
@Controller
@ResponseBody
@CrossOrigin("*")
@RequestMapping("/axshare/subject")
public class SubjectController {
    @Autowired
    SubjectMapper subjectMapper;

    @PostMapping("/addSubject")
    public R addSubject(@RequestBody Subject subject){
        subject.setCreatetime(new Date());
        subject.setModifytime(new Date());
        int insert = subjectMapper.insert(subject);
        HashMap<String, Object> map = new HashMap<>();
        map.put("code",20000);
        map.put("key",1856);
        return R.ok(map);


    }
    @PostMapping("/updataSubject")
    public R updataSubject(@RequestBody Subject subject){
        subject.setModifytime(new Date());
        subjectMapper.updateById(subject);
        HashMap<String, Object> map = new HashMap<>();
        map.put("code",20000);
        return R.ok(map);
    }

    @PostMapping("/deleteSubject")
    public R deleteSubject(@RequestParam(value = "id") int id){
        subjectMapper.deleteById(id);
        HashMap<String, Object> map = new HashMap<>();
        map.put("code",20000);
        return R.ok(map);
    }

    @GetMapping("/selectAllSubject")
    public R allSubject(){
        QueryWrapper<Subject> objectQueryWrapper = new QueryWrapper<>();
        List<Subject> subject = subjectMapper.selectList(objectQueryWrapper);
        HashMap<String, Object> map = new HashMap<>();
        map.put("code",20000);
        map.put("data",subject);
        System.out.println(subject);
        return R.ok(map);
    }

}
