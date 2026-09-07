package com.example.demo.weather;

import org.springframework.stereotype.Service;

@Service
public class WeatherService {

    public String currentSummary() {
        return "sunny";
    }
}
