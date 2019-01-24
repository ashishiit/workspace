package com.example.demo;

import org.springframework.core.SpringVersion;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.GetMapping;
@RestController
public class Blogcontroller {
	@GetMapping(value="/")
	public String index()
	{
		return "suck my cock";
	}

}
