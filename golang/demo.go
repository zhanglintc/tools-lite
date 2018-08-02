package main

import (
    "fmt"
    "io/ioutil"
    "regexp"
)

func read_file() string {
    b, _ := ioutil.ReadFile("demo_go_input.txt")
    return string(b)
}

func write_file(content string) {
    ioutil.WriteFile("demo_go_output.txt", []byte(content), 0644)
}

func some_magic(content string) string {
    re, _ := regexp.Compile(`<[^/a][^>]*?>|</[^a][^>]*?>`)
    content = re.ReplaceAllString(content, "")

    re, _ = regexp.Compile(`<a.*?(href=".*?").*?>`)
    content = re.ReplaceAllString(content, "<a $1>")

    return content
}

func main() {
    content := read_file()
    content = some_magic(content)
    fmt.Println(content)
    write_file(content)
}
