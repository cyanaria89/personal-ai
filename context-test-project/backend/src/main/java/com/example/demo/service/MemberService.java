package com.example.demo.service;

import com.example.demo.dto.SignupRequest;
import com.example.demo.dto.SignupResponse;
import com.example.demo.entity.Member;
import com.example.demo.repository.MemberRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
@RequiredArgsConstructor
public class MemberService {

    private final MemberRepository memberRepository;
    private final PasswordEncoder passwordEncoder;

    @Transactional
    public SignupResponse signup(SignupRequest request) {
        memberRepository.findByLoginId(request.loginId())
            .ifPresent(existing -> {
                throw new IllegalArgumentException("이미 사용 중인 loginId입니다.");
            });

        Member member = new Member(
            request.loginId(),
            passwordEncoder.encode(request.password()),
            request.memberName()
        );
        Member savedMember = memberRepository.save(member);

        return new SignupResponse(
            savedMember.getId(),
            savedMember.getLoginId(),
            savedMember.getMemberName()
        );
    }
}
