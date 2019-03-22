import json

lock_tests = [
    ## vulnerable plugin
    {
        "file_contents": json.dumps({
            "packages": [
                {
                    "name": "wpackagist-plugin/jetpack",
                    "version": "5.1",
                    "type": "wordpress-plugin"
                }
            ]
        }),
        "args": [],
        "return_code": 1,
        "text_search": "VULNERABILITY FOUND!!!",
        "vuln_url": "https://wpvulndb.com/vulnerabilities/9168"
    },
    ## vulnerable plugin, no fail arg
    {
        "file_contents": json.dumps({
            "packages": [
                {
                    "name": "wpackagist-plugin/jetpack",
                    "version": "5.1",
                    "type": "wordpress-plugin"
                }
            ]
        }),
        "args": ["--no-fail"],
        "return_code": 0,
        "text_search": "VULNERABILITY FOUND!!!",
        "vuln_url": "https://wpvulndb.com/vulnerabilities/9168"
    },
    {
        # vulnerable plugin
        "file_contents": json.dumps({
            "packages": [
                {
                    "name": "wpackagist-plugin/jetpack",
                    "version": "6.5",
                    "type": "wordpress-plugin"
                }
            ]
        }),
        "args": [],
        "return_code": 0,
        "text_search": "",
        "vuln_url": ""
    }
]
