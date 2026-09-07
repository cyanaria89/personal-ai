package com.example.demo.dto;

import jakarta.validation.constraints.NotBlank;

public record SignupRequest(
    @NotBlank String loginId,
    @NotBlank String password,
    @NotBlank String memberName
) {
}
