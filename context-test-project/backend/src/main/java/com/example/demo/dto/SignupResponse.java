package com.example.demo.dto;

public record SignupResponse(
    Long id,
    String loginId,
    String memberName
) {
}
