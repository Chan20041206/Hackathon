package test;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class type {
    public static void main(String[] args) {
        String csvFilePath = "data.csv"; // CSV 파일 경로
        List<List<String>> data = new ArrayList<>(); // 2차원 리스트 생성

        try (BufferedReader br = new BufferedReader(new FileReader(csvFilePath))) {
            String line;

            while ((line = br.readLine()) != null) {
                String[] values = line.split(","); // CSV 파일에서 한 줄씩 읽어서 ','로 구분하여 문자열 배열로 변환
                List<String> row = new ArrayList<>();

                for (String value : values) {
                    row.add(value);
                }

                data.add(row); // 한 줄씩 2차원 리스트에 추가
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        // 2차원 리스트 출력
        for (List<String> row : data) {
            System.out.println(row);
        }
    }
}

