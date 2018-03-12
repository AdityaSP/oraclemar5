def report(data):
    with open('template/myreport.html') as fh:
        s = fh.read()
        for k,v in data.items():
            s = s.replace('{{'+k+'}}', v)
        with open('reports/myreport_processed.html', 'wt') as output:
            output.write(s)