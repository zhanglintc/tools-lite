class ArticlesController < ApplicationController
  def new
  end

  def create
    @article = Article.new(article_params)
   
    # puts "partial path before: " + @article.to_partial_path.to_s
    # puts "param before: " + @article.to_param.to_s
    puts "url before: " + url_for(@article).to_s
    @article.save
    # puts "partial path after: " + @article.to_partial_path.to_s
    # puts "param after: " + @article.to_param.to_s
    puts "url after: " + url_for(@article).to_s

    redirect_to @article
  end

  def show
    @article = Article.find(params[:id])
  end

  def index
    @articles = Article.all
  end

  private
    def article_params
      params.require(:article).permit(:title, :text)
    end
end
