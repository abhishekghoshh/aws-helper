package io.github.abhishekghoshh.aws.s3;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Profile;
import software.amazon.awssdk.auth.credentials.AwsBasicCredentials;
import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.auth.credentials.StaticCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;

@Configuration
public class S3Config {

    @Value("${cloud.aws.region.static}")
    private String region;

    @Bean("s3Client")
    @Profile("local")
    public S3Client localS3Client(@Value("${cloud.aws.credentials.accessKey}") String accessKey,
                                  @Value("${cloud.aws.credentials.secretKey}") String secretKey) {
        AwsBasicCredentials basicCredentials = AwsBasicCredentials.create(accessKey, secretKey);
        Region defaultRegion = Region.of(region);
        return S3Client.builder()
                .credentialsProvider(StaticCredentialsProvider.create(basicCredentials))
                .region(defaultRegion)
                .build();
    }

    @Bean("s3Client")
    @Profile("dev")
    public S3Client devS3Client() {
        Region defaultRegion = Region.of(region);
        return S3Client.builder()
                .credentialsProvider(DefaultCredentialsProvider.builder().build())
                .region(defaultRegion)
                .build();
    }
}
