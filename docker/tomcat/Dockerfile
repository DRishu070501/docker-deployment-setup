FROM tomcat:9.0-jdk8

RUN rm -rf /usr/local/tomcat/webapps/*

COPY ../../assets/mysql-connector-j-8.0.33.jar /usr/local/tomcat/lib/

COPY ../../assets/app.war /usr/local/tomcat/webapps/ROOT.war

EXPOSE 8080
