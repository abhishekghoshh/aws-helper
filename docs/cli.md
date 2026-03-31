# AWS CLI access



## Medium

- [How to set up AWS CLI with AWS Single Sign-On (SSO)](https://pushkar-sre.medium.com/how-to-set-up-aws-cli-with-aws-single-sign-on-sso-acf4dd88e056)


## Youtube

- [How to configure AWS CLI so that we can use AWS SSO.](https://www.youtube.com/watch?v=8NjffR4-ils)



## Theory

Configure AWS cli with access id and key
```bash
> aws configure
AWS Access Key ID [None]: ********************
AWS Secret Access Key [None]: ****************************************
Default region name [None]: us-east-1
Default output format [None]: json
```

Check aws configured user
```zsh
> aws sts get-caller-identity
{
    "UserId": "#####",
    "Account": "#####",
    "Arn": "arn:aws:iam::####:user/####"
}
```